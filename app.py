#from crypto.key_manager import generate_keys

#generate_keys()

#from crypto.signer import sign_document

#sign_document("uploads/sample.txt")

from crypto.verifier import verify_signature

verify_signature(
    "uploads/sample.txt",
    "crypto/signatures/sample.sig"
)