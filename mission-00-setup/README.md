# Mission 0 — Create Your GitHub Workspace

## 1. Task / objective
Create a correctly named repository (`digital-detective-8061`), verify Python and Git tools, prepare the mission folder structure, and publish the repository to GitHub.

## 2. Work completed
- Decided repository name according to rules: `digital-detective-8061` (assignment name + last 4 digits of USN).
- Checked local tool installations (Python 3 and Git).
- Created folder structure for all missions (Mission 0 through Mission 8 and `evidence/`).
- Initialized local Git repository, created initial structure, and connected to GitHub.

## 3. Commands / tools used

| Tool / Command | Purpose / Version |
|---|---|
| `git --version` | Checked Git version: `git version 2.54.0 (Apple Git-157)` |
| `python3 --version` | Checked Python 3 version: `Python 3.9.6` |
| `mkdir` / `touch` | Created mission directories and markdown documentation files. |
| `git init` / `git remote add` | Initialized repository and linked local workspace to GitHub remote. |
| `git pull --no-rebase origin main --allow-unrelated-histories` | Merged initial GitHub README with local repository structure. |

## 4. My understanding
- **What a repository is:** A repository stores versions of folders and files, tracking all changes made over time so developers can collaborate safely.
- **Why folders are organized by mission:** Organizing by missions keeps work, evidence, and code separated according to each learning module, making the project clean and easy to navigate.

## 5. Difficulties faced
- An initial README was accidentally created on GitHub when creating the repository, causing a conflict when pushing the local repository structure because they had no common commit history.

## 6. How I resolved them
- Used `git pull --no-rebase origin main --allow-unrelated-histories` to successfully merge the remote and local histories without rebasing.

## 7. Evidence / files
- `mission-00-setup`
- `README.md`

## 8. Commit details
- **Commit message:** Set up Digital Detective mission structure
- **Branch:** main
- **Repository:** digital-detective-8061
- **Status:** Pushed to GitHub.
