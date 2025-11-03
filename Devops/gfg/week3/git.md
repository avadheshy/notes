# What is GIT ?
Git is a version control system (VCS) — a tool that helps developers track and manage changes to their code over time.

### Think of it like a time machine for your code — it lets you:

- Save different versions (called commits) of your project.

- Go back to previous versions if something breaks.

- Work on new features in separate branches without disturbing the main code.

- Merge changes from multiple developers smoothly.

# What is Github ?
GitHub is a cloud platform that hosts your Git repositories online.

While Git works locally on your computer, GitHub helps you:
- Store your repositories in the cloud

- Collaborate with others (pull requests, issues, reviews)

- Share your work publicly or privately

- Integrate with CI/CD tools (like GitHub Actions)
  
# What is Git three-stage Architecture ?
Git has a three-stage architecture, consisting of the working directory, the staging area, and the repository.

## 1. Working Directory :
Any changes made to files in the working directory are not yet tracked by Git.

## 2. Staging Area :
Staging Area is used to prepare changes before they are committed to the repository. Developers can selectively choose which changes to commit by adding them to the staging area.

## 3 Repository (git directory) :
The repository is where Git stores the history of changes made to the codebase. It contains all versions of the codebase, including the current version and all previous versions. When a developer makes a commit, Git takes the changes from the staging area and creates a snapshot of the project, which is then stored in the repository.

# Working with Git stash and Git pop
- git stash is a temporary storage feature in Git.
- It lets you save your uncommitted changes (both staged and unstaged) without committing them — and gives you a clean working directory.
### Save (stash) your changes
```
git stash
```
### List your stashes
```
git stash list
```
### Apply or Pop your stash
```
git stash apply # This re-applies the latest stash but keeps it saved, in case you want to reuse it.

git stash pop # This re-applies the stash and removes it from the stash list.


git stash drop stash@{1} # If you want to delete a specific stash

git stash clear # To delete all stashes:

```
# What is a Merge Conflict?

A merge conflict happens when Git cannot automatically combine changes from two different branches because the same part of a file was modified in both branches differently.

# What is Git Revert and Reset (Reset vs Revert) & Ammend ?

git revert <commit_hash> is used when you want to undo the effects of a specific commit, but keep history clean and safe.

Instead of deleting history, Git makes a new commit that “cancels out” the previous one.

---
git reset moves your branch pointer (like main or feature-x) backward or to a specific commit.
```
git reset [--soft | --mixed | --hard] <commit_hash>
```
| Mode                | What happens to commits                   | What happens to files       |
| ------------------- | ----------------------------------------- | --------------------------- |
| `--soft`            | Commits are undone                        | Changes remain **staged**   |
| `--mixed` (default) | Commits undone                            | Changes remain **unstaged** |
| `--hard`            | Commits & changes **deleted permanently** | ⚠️ Danger zone              |

```
git reset --soft HEAD~1   # Undo last commit but keep changes staged

git reset --hard HEAD~1   # Completely remove last commit and its changes
```
---
Use git commit --amend when you:

- Forgot to add a file to your last commit

- Misspelled a commit message

- Want to slightly modify the most recent commit

---
# What is Git Rebase?
git rebase is a Git command that lets you move or “replay” commits from one branch onto another branch.

“Take all the changes from my branch and reapply them on top of another branch’s latest state.”

It keeps your commit history clean and linear — no unnecessary “merge commits.”

---
## Example Scenario
Let’s say you have:
```
main:    A --- B --- C
feature:        \ 
                  D --- E
```
Now, while you were working on your feature branch (D and E),
someone added new commits (C) to main.

If you run:
```
git checkout feature
git rebase main
```
Git will:
- Take commits D and E
- Temporarily remove them
- Apply commits A, B, C
- Replay D and E on top
  
Resulting in:
```
main:    A --- B --- C
feature:              \
                       D' --- E'

```
### Basic Rebase Commands
#### 1. Start a rebase 
```
git rebase main

# Replays your commits on top of the main branch.
```
#### 2️. Continue after fixing conflicts
```
git rebase --continue
# If there’s a merge conflict, Git pauses.
# You fix the conflict manually, then run this to proceed.
```
#### 3. Skip a commit
```
git rebase --skip
# Skip the problematic commit during rebase.
```
### 4. Abort rebase
```
git rebase --abort
# Cancel rebase and return to the original branch state.
```
#### 5.  Interactive Rebase (git rebase -i)
You can also edit, squash, or reorder commits using:
```
git rebase -i HEAD~3
```
You’ll see a list like:
```
pick a1b2c3 Add login API
pick d4e5f6 Add logout API
pick g7h8i9 Fix typo
```
# what happen
when i am on main branch and run this command
```
git rebase feature
```
So Git will:

- Find the common ancestor of both branches → commit B

- Identify commits on main after B → C

- Temporarily remove commit C

- Move the main branch pointer to the tip of feature (commit E)

- Replay commit C on top of E
  
---
# What is Git Squash?

Git squash means combining multiple commits into one single commit.

- “I made five small, messy commits while developing a feature — now I want to merge them into one clean commit before sharing.”
```
For example, if you want to squash the last 3 commits:

git rebase -i HEAD~3
```
### Shortcut: Squash During Merge
If you don’t want to manually rebase, you can squash when merging a feature branch:
```
git checkout main
git merge --squash feature
git commit -m "Add new API feature"
```

# What is git cherry-pick ?
git cherry-pick is a Git command that lets you selectively apply specific commits from one branch onto another.

| Command                                | Description                                               |
| -------------------------------------- | --------------------------------------------------------- |
| `git cherry-pick <commit>`             | Apply a single commit                                     |
| `git cherry-pick A..B`                 | Apply all commits from `A` (exclusive) to `B` (inclusive) |
| `git cherry-pick --no-commit <commit>` | Apply changes without creating a new commit yet           |
| `git cherry-pick --continue`           | Continue after resolving conflicts                        |
| `git cherry-pick --abort`              | Abort an ongoing cherry-pick process                      |

# What is Git fork? 
A fork in Git (especially on platforms like GitHub, GitLab, or Bitbucket) is a copy of someone else’s repository into your own account — allowing you to freely make changes without affecting the original project.