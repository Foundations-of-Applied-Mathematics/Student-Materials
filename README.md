This repository contains specifications files for the Foundations of Applied Mathematics labs.
Skip down to [Setup](#setup) for setup instructions.

The labs in this curriculum aim to introduce computational and mathematical concepts, walk through implementations of those concepts in Python, and use industrial-grade code to solve interesting, relevant problems.
Lab assignments are usually about 5-10 pages long and include code examples (yellow boxes), important notes (green boxes), warnings about common errors (red boxes), and about 3-7 exercises (blue boxes).
The lab manuals can be downloaded from [foundations-of-applied-mathematics.github.io](http://foundations-of-applied-mathematics.github.io/).

**Contents**

- [Submitting Assignments](#submitting-assignments)
    - [Labs](#labs)
    - [Homework](#homework)
- [Setup](#setup)
- [Using Git](#using-git)
    - [Common Git Commands](#common-git-commands)
    - [Example Work Session](#example-work-session)

# Submitting Assignments

### Labs

Every lab has a corresponding specifications file with some code to get you started and to make your submission compatible with automated test drivers.
Like the lab manuals, these materials are hosted at [foundations-of-applied-mathematics.github.io](http://foundations-of-applied-mathematics.github.io/).

Download the `.zip` file for your course, unzip the folder, and move it somewhere where it won't get lost.
This folder has some setup scripts and a collection of folders, one per lab, each of which contains the specifications file(s) for that lab.
See [Student-Materials/wiki/Lab-Index](https://github.com/Foundations-of-Applied-Mathematics/Student-Materials/wiki/Lab-Index) for the complete list of labs, their specifications and data files, and the manual that each lab belongs to.

**_WARNING:_** Do **not** move or rename the lab folders or the enclosed specifications files; if you do, the test drivers will not be able to find your assignment.
Make sure your folder and file names match [Student-Materials/wiki/Lab-Index](https://github.com/Foundations-of-Applied-Mathematics/Student-Materials/wiki/Lab-Index).

Labs are submitted via git.
To submit a lab, modify the provided specifications file and add, commit, and push the changes (see [Using Git](#using-git) for details on using git).
The instructor will drop feedback files in the lab folder after grading the assignment.
For example, the Introduction to Python lab has `PythonIntro/python_intro.py` as its specifications file.
To complete that assignment, modify `PythonIntro/python_intro.py` and track the changes in git.
After grading, the instructor will create a file called `PythonIntro/PythonIntro_feedback.txt` with your score and some feedback.

### Homework

Non-lab coding homework should be placed in the `_Homework/` folder and submitted via git like a lab assignment.
Be careful to name your assignment correctly so the instructor (and test driver) can find it.
The instructor may drop specifications files and/or feedback files in this folder as well.

# Setup

**_WARNING_**: We strongly recommend using a Unix-based operating system (Mac or Linux) for the labs.
Unix has a true bash terminal, works well with git and python, and is the preferred platform for computational and data scientists.
It is possible to do this curriculum with Windows, but expect some road bumps along the way.

This website is a _git repository_, an online storage place for code and other small files.
_Git_ is the underlying program that manages updates between this online repository and the copies of the repository, called _clones_, stored locally on computers.
If git is not already installed on your computer, download it at [http://git-scm.com/downloads](http://git-scm.com/downloads).
If you have never used git, you might want to read a few of the following resources.

- [Official git tutorial](https://git-scm.com/docs/gittutorial)
- [Bitbucket git tutorials](https://www.atlassian.com/git/tutorials)
- [GitHub git cheat sheet](https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf)
- [GitLab git tutorial](https://docs.gitlab.com/ce/gitlab-basics/start-using-git.html)
- [Codecademy git lesson](https://www.codecademy.com/learn/learn-git)
- [Training video series by GitHub](https://www.youtube.com/playlist?list=PLg7s6cbtAD15G8lNyoaYDuKZSKyJrgwB-)

There are many websites for hosting online git repositories.
Your instructor will indicate which web service to use, but we only include instructions here for setup with Bitbucket.

1. _Sign up_. Create a Bitbucket account at [https://bitbucket.org](https://bitbucket.org).
If you use an academic email address (ending in `.edu`, etc.), you will get free unlimited public and private repositories.

2. _Make a new repository_.
On the Bitbucket page, click the **+** button from the menu on the left and, under **CREATE**, select **Repository**.
Provide a name for the repository, mark the repository as **private**, and make sure the repository type is **Git**.
For **Include a README?**, select **No** (if you accidentally include a README, delete the repository and start over).
For **Include a .gitignore?**, select **No** (if you accidentally include a .gitignore, delete the repository and start over).
Under **Advanced settings**, enter a short description for your repository, select **No forks** under forking, and select **Python** as the language.
Finally, click the blue **Create repository** button.
Take note of the URL of the webpage that is created; it should be something like `https://bitbucket.org/<name>/<repo>`.

3. _Give the instructor access to your repository_.
On your newly created Bitbucket repository page (`https://bitbucket.org/<name>/<repo>` or similar), go to **Settings** in the menu to the left and select **User and group access**, the second option from the top.
Enter your instructor's Bitbucket username under **Users** and click **Add**.
Select the blue **Write** button so your instructor can read from and write feedback to your repository.

4. _Connect your folder to the new repository_.
In a shell application (Terminal on Linux or Mac, or [Git Bash](https://gitforwindows.org/) on Windows), enter the following commands.

```bash
# Navigate to your folder.
$ cd /path/to/folder  # cd means 'change directory'.

# Make sure you are in the right place.
$ pwd                 # pwd means 'print working directory'.
/path/to/folder
$ ls *.md             # ls means 'list files'.
README.md             # This means README.md is in the working directory.

# Connect this folder to the online repository.
$ git init
$ git remote add origin https://<name>@bitbucket.org/<name>/<repo>.git

# Record your credentials.
$ git config --local user.name "your name"
$ git config --local user.email "your email"

# Add the contents of this folder to git and update the repository.
$ git add --all
$ git commit -m "initial commit"
$ git push origin master
```

For example, if your Bitbucket username is `greek314`, the repository is called `acmev1`, and the folder is called `Student-Materials/` and is on the desktop, enter the following commands.

```bash
# Navigate to the folder.
$ cd ~/Desktop/Student-Materials

# Make sure this is the right place.
$ pwd
/Users/Archimedes/Desktop/Student-Materials
$ ls *.md
README.md

# Connect this folder to the online repository.
$ git init
$ git remote add origin https://greek314@bitbucket.org/greek314/acmev1.git

# Record credentials.
$ git config --local user.name "archimedes"
$ git config --local user.email "greek314@example.com"

# Add the contents of this folder to git and update the repository.
$ git add --all
$ git commit -m "initial commit"
$ git push origin master
```

If you enter the repository URL incorrectly in the `git remote add origin` step, you can reset it with the following line.
```bash
$ git remote set-url origin https://<name>@bitbucket.org/<name>/<repo>.git
```

5. _Download data files_.
Many labs have accompanying data files.
To download these files, navigate to your clone and run the `download_data.sh` bash script, which downloads the files and places them in the correct lab folder for you.

```bash
# Navigate to your folder and run the script.
$ cd /path/to/folder
$ bash download_data.sh
```

You can also find individual data files through [Student-Materials/wiki/Lab-Index](https://github.com/Foundations-of-Applied-Mathematics/Student-Materials/wiki/Lab-Index).

6. _Install Python package dependencies_.
The labs require several third-party Python packages that don't come bundled with Anaconda.
Run the following command to install the necessary packages.
```bash
# Navigate to your folder and run the script.
$ cd /path/to/folder
$ bash install_dependencies.sh
```

7. (Optional) _Clone your repository_.
If you want your repository on another computer after completing steps 1-4, use the following commands.

```bash
# Navigate to where you want to put the folder.
$ cd ~/Desktop/or/something/

# Clone the folder from the online repository.
$ git clone https://<name>@bitbucket.org/<name>/<repo>.git <foldername>

# Record your credentials in the new folder.
$ cd <foldername>
$ git config --local user.name "your name"
$ git config --local user.email "your email"

# Download data files to the new folder.
$ bash download_data.sh
```

# Using Git

Git manages the history of a file system through _commits_, or checkpoints.
Use `git status` to see the files that have been changed since the last commit.
These changes are then moved to the _staging area_, a list of files to save during the next commit, with `git add <filename(s)>`.
Save the changes in the staging area with `git commit -m "<A brief message describing the changes>"`.

All of these commands are done within a clone of the repository, stored somewhere on a computer.
This repository must be manually synchronized with the online repository via two other git commands: `git pull origin master`, to pull updates from the web to the computer; and `git push origin master`, to push updates from the computer to the web.

### Common Git Commands

| Command | Explanation |
|:--------|:------------|
| `git status` | Display the staging area and untracked changes. |
| `git pull origin master` | Pull changes from the online repository. |
| `git push origin master` | Push changes to the online repository. |
| `git add <filename(s)>` | Add a file or files to the staging area. |
| `git add -u` | Add all modified, tracked files to the staging area. |
| `git commit -m "<message>"` | Save the changes in the staging area with a given message. |
| `git checkout -- <filename>` | Revert changes to an unstaged file since the last commit. |
| `git reset HEAD -- <filename>` | Remove a file from the staging area. |
| `git diff <filename>` | See the changes to an unstaged file since the last commit. |
| `git diff --cached <filename>` | See the changes to a staged file since the last commit. |
| `git config --local <option>` | Record your credentials (`user.name`, `user.email`, etc.). |

**_NOTE_**: When pulling updates with `git pull origin master`, your terminal may sometimes display the following message.
```bash
Merge branch 'master' of https://bitbucket.org/<name>/<repo> into master

# Please enter a commit message to explain why this merge is necessary,
# especially if it merges an updated upstream into a topic branch.
#
# Lines starting with '#' will be ignored, and an empty message aborts
# the commit.
~
~
```
This means that someone else (the instructor) has pushed a commit that you do not yet have, while you have also made one or more commits locally that they do not have.
This screen, displayed in [_vim_](https://en.wikipedia.org/wiki/Vim_(text_editor)), is asking you to enter a message (or use the default message) to create a _merge commit_ that will reconcile both changes.
To close this screen and create the merge commit, type `:wq` and press `enter`.

### Example Work Session

Short version:
```bash
$ cd ~/Desktop/Student-Materials/
$ git pull origin master                           # Pull updates.

# Make changes to a file.

# Record the changes in git.
$ git add -u                                       # Track changes.
$ git commit -m "Made some changes."               # Commit changes.
$ git push origin master                           # Push updates.
```

Long version:
```bash
# Navigate to the clone of the repository.
$ cd ~/Desktop/Student-Materials/

# Pull any updates from the online repository (such as TA feedback).
$ git pull origin master
From https://bitbucket.org/username/repo
 * branch            master     -> FETCH_HEAD
Already up-to-date.

# Work on the labs. For example, modify PythonIntro/python_intro.py.

$ git status
On branch master
Your branch is up-to-date with 'origin/master'.
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

    PythonIntro/python_intro.py

# Track the changes with git.
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
 1 file changed, 10 insertion(+) 1 deletion(-)

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
