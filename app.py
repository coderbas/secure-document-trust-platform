from pathlib import Path

from flask import (
    Flask,
    render_template,
    request
)

from services.document_service import DocumentService
from crypto.verifier import verify_signature

app = Flask(__name__)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

service = DocumentService()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/verify-page")
def verify_page():
    return render_template("verify.html")

@app.route("/upload", methods=["POST"])
def upload_document():

    file = request.files["document"]

    file_path = UPLOAD_DIR / file.filename

    file.save(file_path)

    signature_path = service.sign(file_path)

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

    document_path = UPLOAD_DIR / document.filename

    signature_path = (
        Path("signatures") /
        signature.filename
    )

    document.save(document_path)
    signature.save(signature_path)

    result = verify_signature(
        document_path,
        signature_path
    )

    if result:
        message = "✓ VALID SIGNATURE"
    else:
        message = "✗ INVALID SIGNATURE"

    return render_template(
        "result.html",
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)