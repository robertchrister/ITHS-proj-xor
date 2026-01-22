import argparse
from xor_core import xor_bytes

# tar emot en sträng bytes i retur
# CLI-argument (argparse) kommer alltid in som strängar
# xor funktionen tar in bytes
# Detta kallas för separation of concerns (miktronivå)
def parse_key(key: str) -> bytes:
    # allow hex or ascii
    # man vet inte om key är giltig hex eller text
    # man skulle kunna använda flaggor här låter vi python prova
    # strängen inte är giltig hex kasta ett undantag
    try:
        return bytes.fromhex(key)
    except ValueError:
        return key.encode()


def main():
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