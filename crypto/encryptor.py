from types import NoneType
from pathlib import Path
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
import os

ENCRYPTED_DIR=Path("encrypted")


def generate_aes_key():
    """
    Generate AES-256 key
    """
    return AESGCM.generate_key(bit_length=256)


def encrypt_file(file_path, key):

    ENCRYPTED_DIR.mkdir(exist_ok=True)

    aesgcm=AESGCM(key)

    nonce = os.urandom(12)

    with open(file_path, "rb") as f:
        plaintext= f.read()

    ciphertext = aesgcm.encrypt(nonce, plaintext, None)

    encrypted_file= (
        ENCRYPTED_DIR /
        f"{Path(file_path).stem}.bin"
    )

    with open(encrypted_file, "wb") as f:
        f.write(nonce + ciphertext)

    print(f"Encrypted file saved to: {encrypted_file}")

    return encrypted_file

def decrypt_file(file_path, key):
    aesgcm= AESGCM(key)

    with open(file_path, "rb") as f:
        data= f.read()

    nonce = data[:12]
    ciphertext= data[12:]

    plaintext = aesgcm.decrypt(
        nonce,
        ciphertext,
        None
    )

    return plaintext