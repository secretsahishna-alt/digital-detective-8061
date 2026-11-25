# Mission 5 — Numbers and Data

## 1. Task / objective
Convert decimal, binary and hexadecimal values.Explain character encoding standards.

## 2. Work completed
- **Task 5.1:** Performed manual calculations .
- **Task 5.2:** Verified each manual conversion result using Python.
- **Task 5.3:** Built and tested [`number_converter.py`].
- **Task 5.4:** Solved given questions.

## 3. Commands / tools used

| Command / Function / Tool | Purpose |
|---|---|
| `bin()` | Built-in Python function converting an integer into a binary string prefixed with `0b`. |
| `hex()` | Built-in Python function converting an integer into a hexadecimal string prefixed with `0x`. |
| `int(string, base)` | Built-in Python function parsing a string representation of a number in base 2, 10, or 16 into a decimal integer. |
| `input()` | Captures user keyboard input in the Python interactive terminal. |
| `python3 number_converter.py` | Terminal command used to execute the custom number conversion program. |

## 4. My understanding
- Understood how `bin()` and `hex()` and `int(val, base)`work.
- Understood the importants of  text encoding 

## 5. Difficulties faced
- Handling the prefix notation (`0b` and `0x`) in Python string outputs when displaying raw converted bits and hex characters to the user.

## 6. How I resolved them
- Used string slicing (`[2:]`) to cleanly separate the numeric values from Python's base indicator prefixes in `number_converter.py`.

## 7. Evidence / files
- `number_converter.py`
- ` Task_5.1-1.heic and Task_5.1-1.heic`
-  `Task_5.2.tiff`
- `Task-5.3-Converter-Tests.md`
- `Task-5.4-Text-Encoding.md`
- `README.md`

## 8. Commit details
- **Commit message:** Build number converter and practise data representation
- **Branch:** main
- **Repository:** digital-detective-8061
- **Status:** Ready to commit and push to GitHub.
