# Mission 3 — Understand the Operating System

## 1. Task / objective
To explore the operating system environment, running processes, storage, paths and file permissions, and describe core operating system responsibilities.

## 2. Work Completed
- **Task 3.1:** Explored the operating system.
- **Task 3.2:** Examined active processes, explained what a process is, understood the PID (Process Identifier), and identified foreground and background process examples.
- **Task 3.3:** Demonstrated navigation between folders, explained the difference between absolute and relative paths, and analyzed file permission letters (`r`, `w`, `x`).
- **Task 3.4:** Completed and understood many different tasks of operating system.

## 3. Commands / Tools Used

| Command / Tool | Purpose |
|---|---|
| `sw_vers` / `uname -srm` | Displays OS product name, release version, kernel build, and hardware architecture (`arm64`). |
| `whoami` | Identifies the active user account running commands in the session. |
| `df -h /` | Reports filesystem disk space usage, capacity, and remaining free space in human-readable units. |
| `top -l 1` / `ps aux` | Captures a snapshot of running processes, resource consumption (%CPU, %MEM), and process IDs. |
| `cd` / `pwd` | Navigates the filesystem tree and displays the current working directory path. |
| `ls -l` | Lists files in long format showing file type, permissions, owner, group, size, and modification timestamp. |

## 4. My Understanding
- Understood the operating system various tasks of operating system.
- Learned how the kernel tracks each active program instance using a unique integer PID.
- Understood the difference between an absolute path (originating from `/`) and a relative path (relative to the current working directory).
- Learned the Unix file permissions of  owner, group, and others, using read (`r`), write (`w`), and execute (`x`) permissions.

## 5. Difficulties Faced
- Ensuring that terminal command outputs did not reveal personal identifying information such as local username, device name, or internal paths.
- Forgot commands-`uname -srm`,`df -h /`,`top -l 1` / `ps aux`

## 6. How I Resolved Them
- Replaced all personal user and device identifiers with `[redacted]` per privacy rules and in screenshot with black boxes editing.
- Revised the forgotten commands.

## 7. Evidence / Files
- `Task-3.1-Operating-System.md`
- `Task-3.2-Processes.md`
- `Task-3.3-Paths-Permissions.md`
- `Task-3.4-OS-Responsibilities.md`
- `README.md`
- `Task_3.1.tiff`

## 8. Commit Details
- **Commit message:** Complete operating system and file management mission
- **Branch:** main
- **Repository:** digital-detective-8061
- **Status:** Staged and committed locally, ready to push to GitHub.
