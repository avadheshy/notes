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
# Difference between merge and rebase
Suppose there are 2 branches main and feature. I made 2 commits(A and B) in main branch and 3 commits (C,D&E) in feature branch.when we apply git merge feature main (merging main branch in feature branch). This will merge main branch in feature with new commit. But when we use git rebase main then feature branch commits will be appended on top of main branch and feature branch head will point its last commit with merging main branch in feature. feature branch will look like this (A->B->C->D->E) E will be the head of feature branch.
