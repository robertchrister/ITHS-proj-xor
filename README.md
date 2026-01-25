## Purpose

This project demonstrates how binary data can be transformed to make static identification less trivial, and how executable behavior can be reconstructed and triggered at runtime.

The focus is educational: understanding the difference between **data at rest**, **data in memory**, and **code under execution**.

---

## Architecture Overview

The project is divided into three clearly separated components with explicit responsibilities:

### 1. Payload
- Raw x86 shellcode generated offline
- Treated purely as binary data
- No execution or interpretation occurs at this stage

### 2. XOR Obfuscator (Python)
- Reads raw binary data from file
- Applies an XOR transformation using a repeating key
- Outputs transformed data in various formats (C, Python, raw)
- **No execution or deobfuscation occurs in Python**

### 3. Loader (C)
- Allocates executable memory at runtime
- Restores the original payload by reversing the XOR operation
- Transfers execution to the reconstructed code

---

## Why XOR

XOR is used to illustrate how simple mathematical transformations can alter the static appearance of binary data without changing its runtime behavior once restored.

The project does **not** aim to bypass modern endpoint protection, but to demonstrate concepts relevant to:
- static vs dynamic analysis
- obfuscation vs encryption
- offensive and defensive security reasoning

---

## Project Structure

The project follows a `src/` layout to clearly separate application code from tests and data:

```text

ITHS-proj-xor/
├── src/
│   ├── cli.py            # Single CLI entry point
│   ├── xor_core.py       # Pure XOR logic (no I/O)
│   ├── io_utils.py       # Binary file handling
│   ├── formatters.py     # Output formatting (C / Python / raw)
│   ├── key_utils.py      # Key parsing (hex / text)
│   ├── loader.c          # Runtime loader (C)
│   └── **init**.py
│
├── shellcode.bin         # Example payload (binary data)
├── xored_shellcode.h     # Generated output
├── tests/                # Unit tests for core logic
├── README.md
└── requirements.txt

```

---

## How to Use

### Generate obfuscated shellcode

Run the CLI from the project root:

```bash
python -m src.cli --in shellcode.bin --key deadbeef --out xored_shellcode.h
````

* `--in` : input file containing raw binary data
* `--key`: XOR key (hex string or text)
* `--out`: output file

The tool operates entirely offline and treats all input as data.

---

## Compile loader (Windows example)

```c
cl loader.c /O2 /MT user32.lib
```

The loader performs runtime memory allocation, deobfuscation, and execution.

---

## Educational Context

This project is part of an educational assignment and focuses on understanding:

* Binary data handling
* Runtime behavior vs static analysis
* Separation of data, transformation, and execution
* Defensive and offensive perspectives on obfuscation

---

## Features

* XOR obfuscation with single- or multi-byte keys
* Cyclic key application using modulo arithmetic
* Output formats:

  * Raw bytes
  * C-compatible byte arrays
  * Python byte literals
* Offline use only

---

## Testing

Unit tests are included to verify and document the intended behavior of the XOR core logic.

Tests cover properties such as:

* reversibility of XOR
* correct key cycling
* error handling for invalid input

Tests act as executable documentation and are not required for production execution.

---

## Design Motivation

The project is intentionally built around a minimal and test-driven core.

### Separation of concerns

The XOR logic is implemented as a pure function:

* no file I/O
* no logging
* no CLI awareness

This makes the core easy to reason about, test, and reuse.

### Explicit input handling

Input interpretation (such as hex vs text keys) is handled outside the core logic.
The core only operates on validated byte sequences.

### Explicit error handling

Invalid input (e.g. an empty XOR key) results in clear exceptions rather than implicit behavior.
This makes failures predictable and safe.

### Focus before features

Correctness and clarity are prioritized over feature richness.
The core logic is validated before additional layers are added.


## Reflection & Learning Outcomes

This project was not only an exercise in implementing XOR-based obfuscation, but also an opportunity to practice structured software design, testing, and documentation.

### Use of pytest for verification

The project uses `pytest` to validate the behavior of the core XOR logic.  
Rather than relying on inline comments or manual testing, behavior is defined and verified through executable tests.

The tests focus on properties rather than specific values, including:
- reversibility of the XOR operation
- correct cycling of multi-byte keys using modulo arithmetic
- explicit error handling for invalid input (e.g. empty keys)

Using `pytest` made it possible to reason about the correctness of the core logic independently of the CLI and file I/O layers.  
This reinforced the idea that **tests are a form of documentation**, not just a quality gate.

---

### Type hints and function signatures

The project makes deliberate use of Python type hints, such as:

```python
def xor_bytes(data: bytes, key: bytes) -> bytes:
```

and:

```python
def parse_key(key: str) -> bytes:
```

These annotations serve multiple purposes:

* they document the expected input and output types
* they clarify the responsibility of each function
* they act as design signals for separation of concerns

Functions that accept `str` are associated with user-facing input interpretation, while functions that operate purely on `bytes` are part of the core transformation logic.
This distinction helped guide architectural decisions and prevent unintended coupling between layers.

---

### Separation of concerns in practice

A key learning outcome of this project was understanding how to separate responsibilities across modules:

* `cli.py` handles user interaction and orchestration
* `key_utils.py` interprets human-readable key input
* `xor_core.py` implements the transformation logic without side effects
* `io_utils.py` handles binary file operations
* `formatters.py` focuses on output representation

This structure makes the codebase easier to test, reason about, and extend.
It also allows individual components to be reused in other contexts without modification.

---

### Defensive programming and explicit errors

The core XOR function explicitly validates its input:

```python
if not key:
    raise ValueError("key must not be empty")
```

Even though the CLI already performs input parsing, the core logic defends itself against invalid usage.
This reinforces the principle that **each layer must be correct in isolation**, not only in the intended execution path.

---

### Documentation as a design tool

Writing the README and accompanying documentation helped clarify design decisions and expose inconsistencies early.
The act of documenting the project influenced how responsibilities were distributed across modules and encouraged a cleaner architecture.

In hindsight, documentation and testing were not afterthoughts but integral parts of the development process.

---

### Portfolio relevance

This project demonstrates:

* practical handling of binary data in Python
* test-driven verification using pytest
* conscious use of type hints as design tools
* clear separation between data, transformation, and execution
* the ability to reason about security-related concepts from both offensive and defensive perspectives

The project is intentionally minimal, focusing on correctness and clarity rather than feature breadth.




## Notes

- The XOR obfuscator operates purely on data and never executes input.
- All transformations are reversible by design.
- The Python tooling is platform-independent and does not require Kali Linux.
- The C loader is provided for educational demonstration only.

