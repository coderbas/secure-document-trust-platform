from pathlib import Path

from flask import (
    Flask,
    render_template,
    request
)

from services.document_service import DocumentService


app = Flask(__name__)

UPLOAD_DIR = Path("uploads")
UPLOAD_DIR.mkdir(exist_ok=True)

service = DocumentService()


@app.route("/")
def home():
    return render_template("index.html")


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


if __name__ == "__main__":
    app.run(debug=True)