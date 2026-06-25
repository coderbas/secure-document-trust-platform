# Secure Document Trust Platform
## Development Journal

---

## Day 1 – Project Planning and Cryptographic Foundation

**Date:** 05 June 2026

### Objective
Establish the project architecture, development environment, repository structure, and cryptographic foundation for the Secure Document Trust Platform.

### Activities Completed

#### Project Selection
- Selected the project topic:
  - Secure Document Trust Platform using RSA, AES, and SHA-256.
- Reviewed assignment requirements and ensured the proposed system addresses:
  - Confidentiality
  - Integrity
  - Authentication
  - Non-repudiation

#### System Design
- Designed the high-level architecture of the platform.
- Identified the core system modules:
  - Key Management Module
  - Digital Signature Module
  - Verification Engine
  - Encryption Module
  - Secure Storage Layer
  - Audit Logging Module
  - Web User Interface

#### Development Environment Setup
- Created project workspace.
- Configured Python virtual environment.
- Installed required libraries:
  - Flask
  - cryptography
  - PyCryptodome

#### Repository Setup
- Created GitHub repository:
  - secure-document-trust-platform
- Initialized Git version control.
- Configured .gitignore to exclude:
  - Virtual environment files
  - Cryptographic keys
  - Generated signatures
  - Uploaded documents
  - Encrypted files

#### Cryptographic Foundation
- Implemented RSA Key Management Module.
- Generated RSA-2048 public/private key pair.
- Stored keys in PEM format.
- Implemented functionality for:
  - Key generation
  - Key storage
  - Key loading

### Security Considerations
- Private keys are excluded from version control.
- RSA-2048 selected as the asymmetric cryptographic algorithm.
- Future encryption layer will use AES-256-GCM.
- SHA-256 selected for hashing and integrity verification.

### Challenges Encountered
- Determining an appropriate project scope that balances security, complexity, and implementation effort.
- Designing a modular architecture that can be extended with additional security features later.

### Solutions
- Chose a document trust and verification platform instead of a more complex blockchain or zero-knowledge solution.
- Adopted a modular architecture to separate cryptographic operations from the user interface and storage components.

### Deliverables Completed
- Project architecture finalized.
- Repository initialized.
- Development environment configured.
- RSA key generation module completed.
- Initial project structure established.

### Next Steps
1. Implement SHA-256 document hashing.
2. Implement RSA digital signature generation.
3. Implement signature verification engine.
4. Demonstrate tamper detection using modified documents.

### Milestone Status
✅ Milestone 1: RSA Key Management Module Completed

## Day 2

### Activities Completed

- Implemented RSA digital signature generation module.
- Successfully signed documents using RSA-2048 private key.
- Generated and stored digital signatures in binary (.sig) format.
- Tested signing process on sample document.

### Security Concepts Demonstrated

- Authentication
- Integrity
- Non-repudiation

### Challenges Encountered

- Import error caused by incorrect indentation of key loading functions.

### Resolution

- Moved load_private_key() and load_public_key() functions outside generate_keys().

### Deliverables Completed

- signer.py module implemented.
- Digital signature generation successfully tested.

### Next Steps

- Implement signature verification engine.
- Demonstrate tamper detection.

### Verification Engine

- Implemented RSA signature verification using the public key.
- Successfully validated legitimate signatures.
- Implemented tamper detection functionality.
- Demonstrated that modifying a signed document invalidates its signature.

### Security Properties Demonstrated

- Integrity
- Authentication
- Non-Repudiation

### Testing Results

Test Case 1:
Original document verified successfully.

Result:
✓ VALID

Test Case 2:
Document modified after signing.

Result:
✗ INVALID

Conclusion:
The verification engine successfully detects unauthorized modifications.


ok## Day 3

### Activities Completed

- Implemented AES-256-GCM encryption module.
- Implemented AES-256-GCM decryption module.
- Generated secure AES-256 keys.
- Used randomly generated nonces for each encryption operation.
- Successfully encrypted and decrypted test documents.

### Security Properties Demonstrated

- Confidentiality
- Data Protection

### Testing Results

Test Case 1:
Encrypt document and store encrypted output.

Result:
Success

Test Case 2:
Decrypt encrypted document using correct AES key.

Result:
Original plaintext recovered successfully.

### Security Considerations

- AES-256-GCM selected because it provides confidentiality, integrity, and authenticated encryption.
- Unique nonce generated for each encryption operation.

### Deliverables Completed

- encryptor.py module implemented.
- Encrypted file storage mechanism implemented.
- Decryption workflow validated.

### Next Steps

- Refactor cryptographic modules.
- Design Flask application architecture.
- Build document upload and verification dashboard.

## Day 4

### Activities Completed

- Integrated Flask frontend with cryptographic backend.
- Implemented document upload functionality.
- Implemented web-based document signing workflow.
- Connected uploaded files to RSA signature generation module.
- Successfully generated signatures through the web interface.

### Security Features Demonstrated

- Authentication
- Integrity
- Non-Repudiation

### Testing Results

Test Case:
Upload document through browser interface.

Result:
- File stored successfully.
- Digital signature generated successfully.
- Signature file created and stored.

### Deliverables Completed

- Upload interface implemented.
- Upload-to-sign workflow completed.

## Day 5

### Activities Completed

- Implemented browser-based signature verification portal.
- Added document and signature upload functionality.
- Integrated verification engine with Flask application.
- Successfully verified authentic signed documents.
- Successfully detected tampered documents.

### Testing Results

Test Case 1:
Original signed document.

Result:
✓ VALID SIGNATURE

Test Case 2:
Document modified after signing.

Result:
✗ INVALID SIGNATURE

### Security Properties Demonstrated

- Integrity
- Authentication
- Non-Repudiation
- Tamper Detection

### Deliverables Completed

- Verification portal implemented.
- End-to-end signing and verification workflow completed.

Date: 18 June 2026

Activities Completed

Implemented AES-256-GCM file encryption.
Implemented AES-256-GCM file decryption.
Added Encryption Portal to Flask interface.
Added Decryption Portal to Flask interface.
Integrated audit logging for encryption and decryption events.
Updated dashboard statistics.
Tested encryption and decryption workflow successfully.
Verified digital signature validation and tamper detection.
Fixed routing and key management issues during development.

Outcome

Secure Document Trust Platform now supports confidentiality, integrity, authenticity, and accountability requirements.