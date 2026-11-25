# Mission 6 — Git and GitHub

## 1. Task / objective
Understand version control, stage and commit changes, create a new branch, open a Pull Request on GitHub, and explain the collaboration workflow.

## 2. Work completed
- **Task 6.1:** Documented the basic Git workflow table and explained the distinction between staging (`git add`) and committing (`git commit`).
- **Task 6.2:** Created a new branch named `update-about`, added a "My Learning" section to the root `README.md`, committed the changes, and pushed the branch to GitHub.
- **Task 6.3:** Created a Pull Request from `update-about` into `main` on GitHub, reviewed the changes, merged the PR, and pulled the updated `main` branch locally.
- **Task 6.4:** Built a comprehensive, easy-to-read Git command glossary.

## 3. Commands / tools used

- `git status` `git add <file>` 
- `git commit -m "<msg>"`  
- `git log --oneline` 
- `git checkout -b <branch>`  `git push -u origin <branch>` 
- `git pull origin main` 

## 4. My Understanding
- **Version Control:** Keeps a complete historical log of changes.
- **Branches:** Create an isolated workspace separate from `main`. By which we can make new version.
- **Pull Requests (PR):** A mechanism on GitHub to notify teammates that work on a branch is ready for review, discussion, and approval before merging it into `main`.
- **Staging vs Committing:** Staging is selecting which changed ingredients go into the basket; committing is taking a permanent photo of that basket.

## 5. Difficulties faced
- Making sure the local `main` branch is updated after merging the Pull Request online.

## 6. How I resolved them
- Switched back to `main` with `git checkout main` and ran `git pull origin main` to synchronize local files with the merged changes on GitHub.

## 7. Evidence / files
- `Task-6.1-Git-Workflow.md`
- `Task-6.4-Git-Glossary.md`
- Root `README.md` (updated with "My Learning" section via PR)
- `README.md`

## 8. Commit details
- **Commit message:** Complete Git and GitHub collaboration mission
- **Branch:** main
- **Pull Request status:** Created `update-about` PR into `main` and merged.
- **Repository:** digital-detective-8061
