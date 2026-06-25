from pathlib import Path

from cryptography.hazmat.primitives import hashes 
from cryptography.hazmat.primitives.asymmetric import padding

from crypto.key_manager import load_private_key

SIGNATURE_DIR = Path(__file__).parent / "signatures"

def sign_document(file_path):
    """
    Sign a document using RSA private key.
    """

    SIGNATURE_DIR.mkdir(exist_ok=True)

    private_key = load_private_key()

    with open(file_path, "rb") as f:
        data = f.read()

    signature = private_key.sign(
        data,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    signature_file = (
        SIGNATURE_DIR /
        f"{Path(file_path).stem}.sig"
    )

    with open(signature_file, "wb") as f:
        f.write(signature)

    print(f"Signature saved to: {signature_file}")

    return signature_file
