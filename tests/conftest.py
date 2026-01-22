import sys
from pathlib import Path

print("conftest.py loaded")
"""
pytest configuration file.

This file ensures that the project's source directory (src/)
is added to Python's import path when tests are executed.

Reason:
In a src-layout project, pytest does not automatically include
the src/ directory in sys.path. Without this,
imports like:

    'from src.xor_obfuscator import xor_data'

would fail during test collection.

This file is only used by pytest and has no effect on
normal program execution.
"""

# Add ITHS-PROJ-XOR/src in sys.path since pytest does not find package src
PROJECT_ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = PROJECT_ROOT / "src"

sys.path.insert(0, str(SRC_PATH))
