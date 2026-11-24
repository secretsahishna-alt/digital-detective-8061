# Task 3.3 — Understand paths and permissions

## 1. Directory Navigation Observation

When navigating between the repository root and a subfolder in Terminal:
- Command : `cd mission-03-operating-system`
- Checking path with: `pwd`
  - Output changes from `/Users/[redacted]/Desktop/SNAI!/digital-detective-8061` to `/Users/[redacted]/Desktop/SNAI!/digital-detective-8061/mission-03-operating-system`
- Command to return to parent: `cd ..`
  - Current working directory returns to `/Users/[redacted]/Desktop/SNAI!/digital-detective-8061`

---

## 2. Absolute Path vs Relative Path

| Concept | Explanation | Example from Assignment Folder |
|---|---|---|
| **Absolute Path** | Specifies the complete path starting from the filesystem root directory (`/`). It always points to the exact same file regardless of what directory you are currently in. | `/Users/[redacted]/Desktop/SNAI!/digital-detective-8061/mission-03-operating-system/README.md` |
| **Relative Path** | Specifies the path to a file or folder relative to the current working directory. It does not start with a leading slash and depends entirely on where you are currently located. | From project root: `mission-03-operating-system/README.md` (or `./mission-03-operating-system/README.md`) |

---

## 3. File Permissions Analysis

Inspecting a practice file using `ls -l mission-02-terminal/terminal-practice/Practice.txt`:

```text
-rw-r--r--  1 [redacted]  staff  52 Nov 24 Practice.txt
```

### Breakdown of Permission String (`-rw-r--r--`):
- **First character (`-`):** Indicates a regular file (would be `d` for a directory).
- **Owner permissions (`rw-`):**
  - **Read (`r`):** Enabled — The owner can open and read the file's contents.
  - **Write (`w`):** Enabled — The owner can edit, modify, and save changes to the file.
  - **Execute (`-`):** Disabled — The file is a text document and cannot be executed as a program.
- **Group permissions (`r--`):** Read-only for members of the `staff` group.
- **Others permissions (`r--`):** Read-only for all other users on the system.

### Summary: Can the owner read, write, or execute?
- **Read:** Yes (`r`)
- **Write:** Yes (`w`)
- **Execute:** No (`-`)

---

## 4. Permission Reference Table

| Permission | Meaning | Example |
|---|---|---|
| **r — Read** | Allows a file's contents to be viewed or read. On a directory, allows listing its contents. | Opening or reading a text file with `cat`. |
| **w — Write** | Allows modifying, editing, or deleting a file. On a directory, allows creating/deleting files inside. | Editing and saving changes in a text file. |
| **x — Execute** | Allows a file to be executed as a program or script. On a directory, allows entering/traversing it (`cd`). | Running a Python script or shell script. |
