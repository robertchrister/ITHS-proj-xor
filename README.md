# XOR Shellcode Obfuscator  – Educational Project

## Purpose
This project demonstrates how binary data can be transformed to make static identification less trivial, and how executable behavior can be reconstructed and triggered at runtime.

## Architecture Overview
The project is divided into three clearly separated components:

1. **Payload**
   - Raw x86 shellcode generated offline
   - Represents executable behavior in its simplest form

2. **XOR Obfuscator (Python)**
   - Reads raw shellcode from file
   - Applies XOR transformation using a repeating key
   - Outputs a C-compatible byte array
   - No execution or decryption takes place in Python

3. **Loader (C)**
   - Allocates memory at runtime
   - Restores the executable form of the payload in memory
   - Transfers execution to the reconstructed code

## Why XOR
XOR is used to illustrate how simple mathematical transformations can alter the static appearance of binary data without changing its behavior once restored.

This project does not aim to bypass modern endpoint protection, but to demonstrate fundamental concepts relevant to both offensive and defensive security analysis.

## How to Use

### Generate obfuscated shellcode
```bash
python xor_obfuscator.py --input shellcode.bin --key deadbeef --output xored_shellcode.h
```
## Compile loader (Windows)
```c
cl loader.c /O2 /MT user32.lib
```
## Educational Context

_This project is part of an educational assignment and focuses on understanding:_

- Binary data handling
- Runtime behavior vs static analysis
- Separation of data, transformation, and execution


## Features 
- XOR obfucation with single or multi-byte key
- Output formats: raw, C, Python
- Offline use only


## Testing

Unit tests are included in the repository to document and verify
the intended behavior of the XOR core logic.

Tests are not required for production execution and may be excluded
from deployment packages.

## Design Motivation

This project is intentionally built around a minimal and test-driven core.

### Separation of concerns
The XOR logic is implemented as a pure function without side effects:
- no file I/O
- no logging
- no debug output

This makes the core logic easy to reason about, test, and reuse.

### Test-first verification
All behavioral guarantees (such as reversibility and key cycling) are verified through unit tests rather than inline comments.  
Tests act as executable documentation and define the expected behavior of the system.

### src-layout structure
The project uses a `src/` layout to clearly separate application code from tests and tooling.  
This structure scales well and avoids accidental imports from the project root.

### Explicit error handling
Invalid input (such as an empty XOR key) results in a clear exception rather than implicit or silent behavior.  
This makes failures predictable and safe in production usage.

### Focus before features
Command-line handling and file I/O are intentionally deferred.  
The core logic is validated first to ensure correctness before additional layers are added.


