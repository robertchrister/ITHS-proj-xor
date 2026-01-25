"""
cli.py

Command-line interface for XOR shellcode obfuscation.
"""

import argparse
from pathlib import Path

from src.key_utils import parse_key
from src.xor_core import xor_bytes
from src.io_utils import read_binary_file, write_binary_file
from src.formatters import to_c_array, to_python_bytes, to_raw_hex

def parse_args():
    parser = argparse.ArgumentParser(
        description="XOR-obfuscate shellcode for loader testing"
    )

    parser.add_argument(
        "--in",
        dest="input_file",
        required=True,
        help="Input shellcode file (binary)"
    )

    parser.add_argument(
        "--out",
        dest="output_file",
        required=True,
        help="Output file"
    )

    parser.add_argument(
        "--key",
        required=True,
        help="XOR key (string)"
    )

    parser.add_argument(
        "--format",
        choices=["raw", "c", "py"],
        default="raw",
        help="Output format"
    )

    return parser.parse_args()

def main():
    args = parse_args()

    input_path = Path(args.input_file)
    output_path = Path(args.output_file)
    # key_bytes = args.key.encode("utf-8")
    key_bytes = parse_key(args.key)

    data = read_binary_file(input_path)
    xored = xor_bytes(data, key_bytes)

    if args.format == "raw":
        write_binary_file(output_path, xored)

    elif args.format == "c":
        output_path.write_text(to_c_array(xored))

    elif args.format == "py":
        output_path.write_text(to_python_bytes(xored))

if __name__ == "__main__":
    main()