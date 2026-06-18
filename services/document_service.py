from crypto.signer import sign_document
from crypto.verifier import verify_signature
from crypto.encryptor import (
    generate_aes_key,
    encrypt_file,
    decrypt_and_save
)


class DocumentService:

    def __init__(self):
        self.aes_key = generate_aes_key()

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