"""
xor_core.py

Core XOR logic.
module contains functions only.
file I/O, CLI, formatting in separate files
"""



def xor_bytes(data: bytes, key: bytes) -> bytes:
    """
    XOR a byte sequence using a repeating key.

    :param data: Raw input bytes here shellcode
    :param key: XOR key bytes ValueError if empty
    :return: XOR-transformed bytes
    """
    if not key:
        raise ValueError("key must not be empty")
    
    out = bytearray(len(data))
    key_len = len(key)
   

    # byte = bitstream ^ xor every byte reset cycle with mod key_len
    for i in range(len(data)):
        out[i] = data[i] ^ key[i % key_len]
    
    return bytes(out)



# def verify_xor_failure(shellcode_path: str, key_str: str) -> None:
#     with open(shellcode_path, "rb") as f:
#         original = f.read()

#     correct_key = key_str.encode("utf-8")
#     wrong_key = b"wrongkey"

#     xored = xor_data(original, correct_key)
#     restored_wrong = xor_data(xored, wrong_key)

#     assert original != restored_wrong, "ERROR: XOR restored data with wrong key!"

#     print("[+] Wrong-key test behaved correctly (data differs)")


# def verify_xor_roundtrip(shellcode_path: str, key_str: str) -> None:
#     # Prepare key as bytes
#     with open(shellcode_path, "rb") as f:
#         original = f.read()

#     # XOR obfuscation
#     key = key_str.encode("utf-8")

#     # 3. XOR obfuskering
#     xored = xor_data(original, key)

#     # Restore another XOR
#     restored = xor_data(xored, key)

#     # verify binary identity
#     assert original == restored, "XOR roundtrip failed – data corruption detected"

#     print("[+] XOR roundtrip verification PASSED")





# def main():
#     """
#     Entry point (CLI added later)
#     """
#     pass

# if __name__ == "__main__":
#     verify_xor_roundtrip("shellcode.bin", "secret")
#     verify_xor_failure("shellcode.bin", "secret")