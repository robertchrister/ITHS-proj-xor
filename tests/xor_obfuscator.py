import argparse
from xor_core import xor_bytes


def parse_key(key: str) -> bytes:
    """
    Parse an XOR key provided via the command line.

    The key may be provided either as:
    - a hexadecimal string (e.g. "deadbeef"), or
    - a regular ASCII/UTF-8 string.

    The function always returns the key as a byte sequence
    suitable for XOR operations.

    :param key: XOR key as provided by the user
    :return: Key converted to bytes
    """
    try:
        return bytes.fromhex(key)
    except ValueError:
        return key.encode()


def main():
    """
    Entry point for the XOR obfuscation workflow.

    This function:
    - parses command-line arguments
    - reads raw shellcode from disk
    - applies XOR obfuscation using the provided key
    - writes the result in the requested output format

    No execution or deobfuscation occurs here; the function
    strictly orchestrates data flow between components.
    """
    
    parser = argparse.ArgumentParser(
        description="XOR-obfuscate raw shellcode (offline)"
    )

    parser.add_argument("--input", required=True, help="Raw shellcode (.bin)")
    parser.add_argument("--key", required=True, help="XOR key (hex or ascii)")
    parser.add_argument("--output", required=True, help="Output header (.h)")

    args = parser.parse_args()

    with open(args.input, "rb") as f:
        shellcode = f.read()

    key = parse_key(args.key)
    xored = xor_bytes(shellcode, key)

    with open(args.output, "w") as f:
        f.write("unsigned char xored_shellcode[] = {\n")

        for i, b in enumerate(xored):
            f.write(f"0x{b:02x}, ")
            if (i + 1) % 16 == 0:
                f.write("\n")

        f.write("\n};\n")
        f.write(f"unsigned int xored_shellcode_len = {len(xored)};\n")


if __name__ == "__main__":
    main()