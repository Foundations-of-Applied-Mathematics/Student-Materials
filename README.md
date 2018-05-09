This repository contains specifications files for the Foundations of Applied Mathematics labs.

# Setup

This website is a _git repository_, an online storage place for code and other small files.
_Git_ is the underlying software that manages updates between this online repository and the copies of the repository, called _clones_, stored locally on computers.
If git is not already installed on your computer, download it at http://git-scm.com/downloads.
If you have never used git, you might want to read a few of the following resources.
- https://git-scm.com/docs/gittutorial
- https://www.atlassian.com/git/tutorials
- https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf
- https://docs.gitlab.com/ce/gitlab-basics/start-using-git.html
- https://www.codecademy.com/learn/learn-git

There are many websites for hosting online git repositories.
Your instructor will indicate which web service to use, but we only include instructions here for setup with Bitbucket.

1. _Sign up_. Create a Bitbucket account at https://bitbucket.org.
If you use an academic email address (ending in .edu, ac.il, edu.sg, etc.), you will get free unlimited public and private repositories.

2. _Make a new repository_.
On the Bitbucket page, click the **Repositories** button from the menu at the top and select **Create repository**.
Provide a name for the repository, mark the repository as **private**, and make sure the repository type is **Git**.
Under **Advanced settings**, enter a short description for your repository, select **No forks** under forking, and select **Python** under language.
Finally, click the blue **Create repository** button.
Take note of the URL of the webpage that is created; it should be something like `https://bitbucket.org/username/repo`.

3. _Give the instructor access to your repository_.
On your Bitbucket page (`https://bitbucket.org/username/repo`), click the blue **Send invitation** button at top right part of the page.
Enter your instructor's Bitbucket username and click **Add**.
Select the blue **Write** button (so your instructor can write feedback to your repository) and click **Share**.

4. _Connect your folder to the new repository_.
In a shell application (Terminal on Linux or Mac, or Git Bash on Windows), enter the following commands (here `username` is your Bitbucket username and `repo` is the name of your new repository).

```bash
# Navigate to your folder.
$ cd ~/Desktop/foldername

# Connect this folder with the online repository.
$ git init
$ git remote add origin https://username@bitbucket.org/username/repo.git

# Add your credentials to the folder.
$ git config --local user.name "your name"
$ git config --local user.email "your email"

# Add the contents of this folder to git and update the repository.
$ git add --all
$ git commit -m "initial commit"
$ git push origin master
```

If you enter the repository URL incorrectly, you can reset it with the following line.
```bash
$ git remote set-url origin https://username@bitbucket.org/username/repo.git
```

5. _Download data files_.
Many labs have accompanying data files.
To download these files, navigate to your clone and run the `download_data.sh` bash script, which downloads the files and places them in the correct lab folder for you.

```bash
# Navigate to your folder and run the script.
$ cd ~/Desktop/foldername
$ bash download_data.sh
```

6. (Optional) _Clone your repository_.
If you want your repository on another computer after completing steps 1-4, use the following commands.

```bash
# Clone the folder from the online repository.
$ cd ~/Desktop
$ git clone https://username@bitbucket.org/username/repo.git foldername

# Add your credentials to the new folder.
$ cd foldername
$ git config --local user.name "your name"
$ git config --local user.email "your email"
```
Repeat step 5 in this clone as well.

# Using Git

Git manages the history of a file system through _commits_, or checkpoints.
Use `git status` to see the files that have been changed since the last commit.
These changes are then moved to the _staging area_, a list of files to save during the next commit, with `git add <filename(s)>`.
Save the changes in the staging area with `git commit -m "A brief message describing the changes"`.

All of these commands are done within a clone of the repository, stored somewhere on a computer.
This repository must be manually synchronized with the online repository via two other git commands: `git pull origin master`, to pull updates from the web to the computer; and `git push origin master`, to push updates from the computer to the web.

### Common Git Commands

| Command                     | Explanation                                    |
|:------------------------------------------------|:---------------------------|
| `git status`               | Display the staging area and untracked changes.|
| `git pull origin master`   | Pull down changes from the online repository.  |
| `git push origin master`   | Push up changes to the online repository.      |
| `git add <filename(s)>`    | Add a file or files to the staging area.       |
| `git add -u`               | Add all of the modified, previously tracked files to the staging area.|
| `git commit -m "<message>"` | Save the changes in the staging area with a given message.|
| `git checkout -- <filename>` | Revoke the changes made since the last commit on a file that is not in the staging area. |
| `git reset -- <filename>`  | Remove a file from the staging area.           |
| `git diff <filename>`      | See the changes made on an unstaged file since the last commit.|
| `git diff --cached <filename>` | See the changes made on a staged file since the last commit.|
| `git config --local user.name "your name"` | Record your credentials |
| `git config --local user.email youremail@gmail.com` | Record your credentials |

### Example Work Session

Short version:
```bash
$ cd Desktop/foldername/
$ git pull origin master                           # Pull updates.

# Make changes to a file.

$ git add -u                                       # Track changes.
$ git commit -m "Made some changes."               # Commit changes.
$ git push origin master                           # Push updates.
```

Long version:
```bash
# Navigate to the clone of the repository.
$ cd Desktop/foldername/

# Pull any updates from the online repository (such as TA feedback).
$ git pull origin master
From https://bitbucket.org/username/repo
 * branch            master     -> FETCH_HEAD
Already up-to-date.

# Work on the labs. For example, modify PythonIntro/python_intro.py.

$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Untracked files:
  (use "git add <file>..." to include in what will be committed)

    PythonIntro/python_intro.py

nothing added to commit but untracked files present (use "git add" to track)

$ git add PythonIntro/python_intro.py
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    modified:   PythonIntro/python_intro.py

# Commit the changes to the repository with an informative message.
$ git commit -m "Made some changes"
[master fed9b34] Made some changes
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 python_intro.py

# Push the changes to the online repository.
$ git push origin master
Counting objects: 3, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 327 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://username@bitbucket.org/username/repo.git
   5742a1b..fed9b34  master -> master

# The changes have been saved and the online repository updated.
$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
nothing to commit, working directory clean
```
