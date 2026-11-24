# Task 4.2 — Compare compiler and interpreter

## Comparison Table

| Point | Compiler | Interpreter |
|---|---|---|
| **When translation / execution happens** | Translates the entire source code into machine code or intermediate form before the program is run. | Translates and executes the program instruction-by-instruction at runtime while the program is running. |
| **Typical output** | Standalone executable binary file (e.g., machine code  | Direct output/results generated immediately line-by-line; no separate machine-code binary is created. |
| **One example** | C / C++ | Python |
| **One advantage** | Runs significantly faster and optimizes CPU execution because translation is completed ahead of time. | Rapid testing, prototyping, and easier debugging because code runs immediately without an extra build or compilation step. |

---

## Explanation of Differences

A compiler translates the complete source code of a program into machine code all at once before execution, making a  executable file that the computer's CPU can run directly so its faster. In contrast, an interpreter reads and translates the source code line by line in run time while the program is running. As shown in the comparison table, compiled languages like C or C++ offer superior runtime performance, whereas interpreted languages like Python provide faster development workflows and instant error feedback without requiring a separate compilation step. 
