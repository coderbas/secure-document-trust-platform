from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from pathlib import Path

KEYS_DIR = Path(__file__).parent / "keys"


def generate_keys():

    KEYS_DIR.mkdir(exist_ok=True)
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    public_key = private_key.public_key()

    with open(KEYS_DIR / "private.pem", "wb") as f:
        f.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption()
            )
        )

    with open(KEYS_DIR / "public.pem", "wb") as f:
        f.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )
    
    print("RSA Key pair generated successfully.")

    def load_private_key():
        with open(KEYS_DIR / "private.pem", "rb") as f:
            return serialization.load_pem_private_key(
                f.read(),
                password=None
            )
    
    def load_public_key():
        with open(KEYS_DIR / "public.pem", "rb") as f:
            return serialization.load_pem_public_key(
                f.read()
            )
    
    