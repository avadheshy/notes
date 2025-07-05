- Use reset when you're working alone or on local branches, and use revert when you're working on shared or public branches. 
  
# git revert — Creates a New Commit That Reverses the Changes
 Key Points:
- It does NOT delete or remove the original commit.

Instead, it creates a new commit that adds changes which cancel out the original commit’s changes.

So the original commit still exists in the history — it is not removed.

The codebase state changes, but the history stays intact.

# Example Workflow:
Suppose you have this history:

```
A -- B -- C -- D (HEAD)
#Now you run:
git revert C
# Git will generate a new commit E, such that:

A -- B -- C -- D -- E (HEAD)
# E is a new commit that undoes the changes introduced by commit C.
```
Commit C is still there. It's just that its changes are "cancelled out" by E.
# git cherry-pick <commit>
Use: Apply a specific commit from another branch into your current branch.
```
git checkout feature-branch
git cherry-pick a1b2c3d
```
This applies commit a1b2c3d from any branch to feature-branch, as if it was made there originally.

# Use Cases:
Porting a bug fix from one branch to another.

Applying just one or two useful commits from a long feature branch without merging the whole branch.

# git reset Recap (with HEAD or ID)
```
git reset --soft HEAD~1    # Undo last commit, keep files staged
git reset --mixed HEAD~1   # Undo last commit, keep files but unstage
git reset --hard HEAD~1    # Undo last commit AND all file changes
```
# Difference between centerlized and distributed version controll system?
Centralized version control systems rely on a single server for all operations and require a constant connection, while distributed version control systems allow each user to have a complete local copy of the repository, enabling offline work and greater resilience.

# what is fork?

In software development, a fork refers to creating a personal copy of a repository, often to experiment, make changes, or develop independently, without affecting the original repository.
# difference beteen clone and fork
Use fork to create your version of a repository on the hosting platform.
Use clone to download a repository to your local machine for development.
# what is the use of cherypick(used for less number of commit) why not merge
The git cherry-pick command is used to apply specific commits from one branch into another, whereas git merge combines all changes from one branch into another in one go. Here's why you might prefer cherry-pick over merge for a small number of commits
``` 
git cherry-pick <commit-hash>
```

# git 
Git is a distributed version control system designed to track changes in files, especially code, during software development. It allows multiple developers to collaborate on a project, track changes, and manage different versions of the project over time.GitHub is a web-based platform built around Git. It provides a place to host Git repositories online, facilitating easier collaboration and project management.
## file stages
There are 4 stages in a git repository: 1. Untracked Files which are not added to git repository. 2 Modified have changed from last commit. 3. Indexed These file are ready to go in commit state after commit. 4 Commit : These files are ready to go on github after push.
#  1. SETUP
Configuring user information used across all local repositories
## git config --global user.name “[firstname lastname]”
set a name that is identifiable for credit when review version history
## git config --global user.email “[valid-email]”
set an email address that will be associated with each history marker
## git config --global color.ui auto
set automatic command line coloring for Git for easy reviewing
# 2. SETUP & INIT
Configuring user information, initializing and cloning repositories
## git init
initialize an existing directory as a Git repository
## git clone [url]
retrieve an entire repository from a hosted location via URL
# 3. STAGE & SNAPSHOT
Working with snapshots and the Git staging area
## git status
show modified files in working directory, staged for your next commit
## git add [file]
add a file as it looks now to your next commit (stage)
## git reset [file]
unstage a file while retaining the changes in working directory
## git diff
diff of what is changed but not staged
## git diff --staged
diff of what is staged but not yet commited
## git commit -m “[descriptive message]”
commit your staged content as a new commit snapshot
# 4. BRANCH & MERGE
Isolating work in branches, changing context, and integrating changes
## git branch
list your branches. a * will appear next to the currently active branch
## git branch [branch-name]
create a new branch at the current commit
## git checkout
switch to another branch and check it out into your working directory
## git merge [branch]
merge the specified branch’s history into the current one
# 5. INSPECT & COMPARE
Examining logs, diffs and object information
## git log
Show the commit history of current active branch.

## git log branchB..branchA
Show the commits on branchA which are not on branchB
## git log --follow [file]
show the commits that changed file, even across renames
## git show [SHA]
show any object in Git in human-readable format

# 6. TRACKING PATH CHANGES
Versioning file removes and path changes
# git rm [file]
delete the file from project and stage the removal for commit
# git mv [existing-path] [new-path]
change an existing file path and stage the move
# git log --stat -M
show all commit logs with indication of any paths that moved

# 7. IGNORING PATTERNS
Preventing unintentional staging or commiting of files
```
logs/
*.notes
pattern*/
```
Save a file with desired paterns as .gitignore with either direct string
matches or wildcard globs.

# 8. SHARE & UPDATE
Retrieving updates from another repository and updating local repos
## git remote add [alias] [url]
add a git URL as an alias
## git fetch [alias]
fetch down all the branches from that Git remote
## git merge [alias]/[branch]
merge a remote branch into your current branch to bring it up to date
## git push [alias] [branch]
Transmit local branch commits to the remote repository branch
## git pull
fetch and merge any commits from the tracking remote branch

# 9. REWRITE HISTORY
Rewriting branches, updating commits and clearing history
# git rebase [branch]
apply any commits of current branch ahead of specified one
# git reset --hard [commit]
clear staging area, rewrite working tree from specified commit

# 10. TEMPORARY COMMITS
Temporarily store modified, tracked files in order to change branches
# git stash
Save modified and staged changes
# git stash list
list stack-order of stashed file changes
# git stash pop
it applies the latest stash and removes from the stash list.
# git stash drop
it removes the latest stash without applying it.
# git stash apply
git stash apply applies the most recent stash (the one at the top of the stash stack) to your working directory.
# git stash apply stash@{2}
If you have multiple stashes, you can specify a particular stash to apply by using its reference, such as stash@{0}, stash@{1}, etc.

# Difference between merge and rebase
Suppose there are 2 branches main and feature. I made 2 commits(A and B) in main branch and 3 commits (C,D&E) in feature branch.when we apply git merge feature main (merging main branch in feature branch). This will merge main branch in feature with new commit. But when we use git rebase main then feature branch commits will be appended on top of main branch and feature branch head will point its last commit with merging main branch in feature. feature branch will look like this (A->B->C->D->E) E will be the head of feature branch.

---
Rebase: Reapply commits on top of another base branch (git rebase <branch>).
