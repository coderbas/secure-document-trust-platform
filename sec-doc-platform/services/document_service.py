from crypto.signer import sign_document
from crypto.verifier import verify_signature
from crypto.aes_key_manager import load_or_create_key
from crypto.encryptor import (
    encrypt_file,
    decrypt_and_save
)


class DocumentService:

    def __init__(self):
        # Loads the same AES key every time the app starts, instead of
        # generating a brand new one each run (which would make every
        # previously-encrypted file permanently undecryptable).
        self.aes_key = load_or_create_key()

    def sign(self, file_path):
        return sign_document(file_path)

    def verify(self, file_path, signature_path):
        return verify_signature(
            file_path,
            signature_path
        )

    def encrypt(self, file_path):
        return encrypt_file(
            file_path,
            self.aes_key
        )

    def decrypt(self, file_path):
        return decrypt_and_save(
            file_path,
            self.aes_key
        )