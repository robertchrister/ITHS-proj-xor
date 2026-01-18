def xor_data(data: bytes, key: bytes) -> bytes:
    """
    XOR-obfuscates data using a repeating key.
    """

    result = bytearray()
    key_len = len(key)

    for i, b in enumerate(data):
        result.append(b ^ key[i % key_len])
    
    return bytes(result)


def main():
    """
    Entry point (CLI added later)
    """
    pass

if __name__ == "__main__":
    main()