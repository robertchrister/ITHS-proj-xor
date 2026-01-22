from xor_obfuscator import xor_data


def test_xor_is_reversible():
    """
    Verifies that XOR is reversible
    """
    data = b"\x90\x90\xcc"
    key = b"\x41"


    xored = xor_data(data, key)
    decoded = xor_data(xored, key)


    assert decoded == data


def test_multibyte_key_cycles_correctly():
    """
    Verifies that the XOR key is applied cyclically.
    Index: 0  1  2  3
    Key:   10 20 10 20
    """
    data = b"\x01\x02\x03\x04"
    key = b"\x10\x20"

    result = xor_data(data, key)

    expected = bytes([
        0x01 ^ 0x10,  # index 0 -> key[0]
        0x02 ^ 0x20,  # index 1 -> key[1]
        0x03 ^ 0x10,  # index 2 -> key[0] reset (cycle)
        0x04 ^ 0x20,  # index 3 -> key[1]
    ])

    assert result == expected

def verify_xor_path(shellcode_path: str, key_str: str) -> None:
    """Read original shellcode in binary mode"""
    with open(shellcode_path, "rb") as f:
        original = f.read()
    
    # Prepare key as bytes
    key = key_str.encode("utf-8")

    # XOR obfuscation
    xored = xor_data(original, key)

    # Restore another XOR
    restored = xor_data(xored, key)

    # verify binary identity
    assert original == restored, "XOR cycle failed - data corruption detected"

    print("[+] XOR cycle verification PASSED")
    