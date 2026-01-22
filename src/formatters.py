"""
formatters.py

Output formatters for XORed shellcode.
"""

def to_c_array(data: bytes, var_name: str = "xored_shellcode") -> str:
    """
    Format bytes as a C unsigned char array.

    :param data: XORed bytes
    :param var_name: C variable name
    :return: C source string
    """
    hex_bytes = ", ".join(f"0x{b:02x}" for b in data)

    return (
        f"unsigned char {var_name}[] = {{\n"
        f"    {hex_bytes}\n"
        f"}};\n"
    )

def to_python_bytes(data: bytes) -> str:
    """
    Format bytes as a Python bytes literal.
    """
    return repr(data)

def to_raw_hex(data: bytes) -> str:
    """
    Format bytes as a continuous hex string.
    """
    return data.hex()
