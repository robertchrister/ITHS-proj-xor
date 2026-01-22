"""
Core XOR transformation logic.

This module contains pure functions only and performs no I/O.
"""


def xor_bytes(data: bytes, key: bytes) -> bytes:
    """
    XOR a byte sequence using a repeating key.

    :param data: Raw input bytes here shellcode
    :param key: XOR key bytes
    :raises ValueError: If the key is empty
    :return: XOR-transformed bytes
    """
    if not key:
        raise ValueError("key must not be empty")
    
    out = bytearray(len(data))
    key_len = len(key)
   

   # Apply XOR byte-by-byte, cycling through the key using modulo
    for i in range(len(data)):
        out[i] = data[i] ^ key[i % key_len]
    
    return bytes(out)