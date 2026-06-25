

from services.database import (
    initialize_database,
    log_operation,
    get_dashboard_stats,
    get_audit_logs

)
from pathlib import Path

from flask import (
    Flask,
    render_template,
    request
)
from werkzeug.utils import secure_filename

from services.document_service import DocumentService
from crypto.verifier import verify_signature

app = Flask(__name__)

initialize_database()

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

service = DocumentService()


@app.route("/")
def home():

    stats = get_dashboard_stats()

    return render_template(
        "index.html",
        stats=stats
    )

@app.route("/verify-page")
def verify_page():
    return render_template("verify.html")

@app.route("/upload", methods=["POST"])
def upload_document():

    file = request.files["document"]

    file_path = UPLOAD_DIR / secure_filename(file.filename)

    file.save(file_path)

    signature_path = service.sign(file_path)

    log_operation(
        "SIGN",
        file.filename,
        "SUCCESS"
    )

    return render_template(
        "result.html",
        message=f"""
        Document uploaded and signed successfully.

        Signature:
        {signature_path}
        """
    )
@app.route("/verify", methods=["POST"])
def verify_document():

    document = request.files["document"]
    signature = request.files["signature"]

    document_path = UPLOAD_DIR / secure_filename(document.filename)

    signature_path = (
        Path("signatures") /
        secure_filename(signature.filename)
    )

    document.save(document_path)
    signature.save(signature_path)

    result = verify_signature(
        document_path,
        signature_path
    )

    log_operation(
        "VERIFY",
        document.filename,
        "VALID" if result else "INVALID"
    )

    if result:
        return render_template(
            "result.html",
            status="valid",
            message="Signature verification successful."
        )

    return render_template(
        "result.html",
        status="invalid",
        message="Document has been modified or signature is incorrect."
    )

@app.route("/audit-logs")
def audit_logs():

    logs = get_audit_logs()

    return render_template(
        "audit_logs.html",
        logs=logs
    )
@app.route("/encrypt-page")
def encrypt_page():
    return render_template("encrypt.html")
@app.route("/encrypt", methods=["POST"])
def encrypt_document():

    document = request.files["document"]

    file_path = UPLOAD_DIR / secure_filename(document.filename)

    document.save(file_path)

    encrypted_file = service.encrypt(file_path)

    log_operation(
        "ENCRYPT",
        document.filename,
        "SUCCESS"
    )

    return render_template(
        "result.html",
        status="success",
        message=f"File encrypted successfully: {encrypted_file}"
    )
@app.route("/decrypt-page")
def decrypt_page():

    return render_template(
        "decrypt.html"
    )
@app.route("/decrypt", methods=["POST"])
def decrypt_document():

    document = request.files["document"]

    encrypted_path = (
        Path("encrypted") /
        secure_filename(document.filename)
    )

    document.save(
        encrypted_path
    )

    decrypted_file = service.decrypt(
        encrypted_path
    )

    log_operation(
        "DECRYPT",
        document.filename,
        "SUCCESS"
    )

    return render_template(
        "result.html",
        status="success",
        message=f"""
        File decrypted successfully.

        Output:
        {decrypted_file}
        """
    )
if __name__ == "__main__":
    app.run(debug=True)