# src/key_utils.py

def parse_key(key: str) -> bytes:
    """
    Parse an XOR key provided via the command line.

    Accepts:
    - hex string (e.g. "deadbeef")
    - ascii/utf-8 string (e.g. "secret")

    Always returns bytes.
    """
    try:
        return bytes.fromhex(key)
    except ValueError:
        return key.encode("utf-8")