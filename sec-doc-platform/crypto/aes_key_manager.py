from pathlib import Path

from cryptography.hazmat.primitives.ciphers.aead import AESGCM

KEYS_DIR = Path(__file__).parent / "keys"
AES_KEY_FILE = KEYS_DIR / "aes_key.bin"


def generate_and_save_key():
    """
    Generate a new AES-256 key and persist it to disk.
    Only call this once during initial setup -- calling it again
    will make all previously encrypted files undecryptable.
    """
    KEYS_DIR.mkdir(exist_ok=True)

    key = AESGCM.generate_key(bit_length=256)

    with open(AES_KEY_FILE, "wb") as f:
        f.write(key)

    print(f"AES-256 key generated and saved to: {AES_KEY_FILE}")

    return key


def load_or_create_key():
    """
    Load the persisted AES key, generating one on first run.
    This is what the app should call at startup, instead of
    generating a fresh key every time the process starts.
    """
    if AES_KEY_FILE.exists():
        with open(AES_KEY_FILE, "rb") as f:
            return f.read()

    return generate_and_save_key()
