from pathlib import Path

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

from crypto.key_manager import load_public_key


def verify_signature(file_path, signature_path):
    """
    Verify a document signature using RSA public key.
    """

    public_key = load_public_key()

    with open(file_path, "rb") as f:
        data = f.read()

    with open(signature_path, "rb") as f:
        signature = f.read()

    try:
        public_key.verify(
            signature,
            data,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        print("✓ Signature is VALID")
        return True

    except InvalidSignature:
        print("✗ Signature is INVALID")
        return False