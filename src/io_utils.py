"""
io_utils.py

Binary-safe file I/O utilities.
"""

from pathlib import Path

def read_binary_file(path: Path) -> bytes:
    """
    Read a file as raw bytes.

    :param path: Path to file
    :return: File content as bytes
    """
    return path.read_bytes()

def write_binary_file(path: Path, data: bytes) -> None:
    """
    Write raw bytes to file.

    :param path: Output file path
    :param data: Bytes to write
    """
    path.write_bytes(data)