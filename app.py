#from crypto.key_manager import generate_keys

#generate_keys()

#from crypto.signer import sign_document

#sign_document("uploads/sample.txt")

#from crypto.verifier import verify_signature

#verify_signature(
 #   "uploads/sample.txt",
 #   "crypto/signatures/sample.sig"
#)

from crypto.encryptor import(
    generate_aes_key,
    encrypt_file,
    decrypt_file
)

key = generate_aes_key()

encrypted_file = encrypt_file(
    "uploads/sample.txt",
    key
)

plaintext = decrypt_file(
    encrypted_file,
    key
)

print("\nRecoveredj Data:")
print(plaintext.decode())
