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

Each course folder has some setup scripts and a collection of folders -- one per lab -- each of which contains the specifications file(s) for that lab.
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
If your computer runs on Windows, we strongly advise you to use Windows Subsystem for Linux (WSL) on Ubuntu.

This website is a _git repository_, an online storage place for code and other small files.
_Git_ is the underlying program that manages updates between this online repository and the copies of the repository, called _clones_, stored locally on computers.
If git is not already installed on your computer, download it with `sudo apt install git` for Linux, or simply type `git` into the terminal on a Mac and follow the prompts.
If you have never used git, you might want to read a few of the following resources.

- [Official git tutorial](https://git-scm.com/docs/gittutorial)
- [GitHub git cheat sheet](https://services.github.com/on-demand/downloads/github-git-cheat-sheet.pdf)
- [GitLab git tutorial](https://docs.gitlab.com/ce/gitlab-basics/start-using-git.html)
- [Bitbucket git tutorials](https://www.atlassian.com/git/tutorials)
- [Codecademy git lesson](https://www.codecademy.com/learn/learn-git)
- [Training video series by GitHub](https://www.youtube.com/playlist?list=PLg7s6cbtAD15G8lNyoaYDuKZSKyJrgwB-)

There are many websites for hosting online git repositories.
Your instructor will indicate which web service to use, but we only include instructions here for setup with GitHub.

You will first need to download the lab materials onto your machine.
The lab manuals can be found at [https://foundations-of-applied-mathematics.github.io/](https://foundations-of-applied-mathematics.github.io/).
You can also download the zip folders that contain the lab materials from this page.
Unzip these folders, and make sure they aren't nested (i.e. make sure there aren't two layers of directories to access the lab materials).


1. _Sign up_. Create a GitHub account at [https://github.com/](https://github.com/).

2. _Create an ssh key_. 
If you have not yet created a GitHub ssh key for your computer, you can do so by running the following command in your terminal:
```bash
$ ssh-keygen -t ecdsa -b 256
```
which will place the key in `~/.ssh`.
Now that the key is created, you need to add it to your GitHub account.
From GitHub, click on your profile icon in the upper right corner, and click on **Settings** towards the bottom of the menu.
Now click on **SSH and GPG keys** on the left, and click the green **New SSH key** button.
Make a Title for this key (it doesn't matter what you put, but you may wish to specify which machine this key will be used for).
Make sure the **Key type** is set to **Authentication Key**.

Now, in your terminal run
```bash
$ cat ~/.ssh/id_ecdsa.pub 
```
Copy everything that's printed out and paste it into GitHub, then press the green **Add SSH key** button.
Then, in your terminal, run
```bash
$ eval $(ssh-agent)
$ ssh-add ~/.ssh/id_ecdsa
```

3. _Make a new repository_.
On your GitHub Home page, click the green **Create repository** button to the upper left of the screen; or, if you have already used GitHub before and already have repositories set up, click on the green **New** button next to **Top Repositories**.
First you will need to provide a Repository name; this can be anything you want, but please make it relevant to the lab folder it will represent; you may also provide a repository description if you like.
Mark the repository as **Private**.
Leave the box next to **Add a README file** unchecked (if you accidentally include a **README**, delete the repository and start over).
Under **Add .gitignore**, select **None** for **.gitignore template** (if you accidentally include a **.gitignore**, delete the repository and start over).
Under **Choose a license**, select **None** for **License**.
Finally, click the green **Create repository** button.

4. _Give the instructor access to your repository_.
In your newly created repository, click the **Settings** tab along the top of the page and click on **Collaborators** on the left.
Then click on the green **Add people** button.
Type your instructor's GitHub username, select them, then click the big green **Add username to this repository** button.


5. _Connect your folder to the new repository_.
In your terminal, enter the following commands.

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
$ git remote add origin git@github.com:<username>/<repo>.git
# Make sure the link has this form. If it starts with https, select the ssh option on GitHub instead.


# Record your credentials. user.name should be your name, and user.email must be the email associated with your GitHub account.
$ git config --global user.name "your name"
$ git config --global user.email "your email"

# Add the contents of this folder to git and update the repository.
$ git add --all
$ git commit -m "initial commit"
$ git push origin main
```

For example, if your GitHub username is `greek314`, the repository is called `acmev1`, and the folder is called `Student-Materials/` and is located in `Desktop`, you would enter the following commands:

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
$ git remote add origin git@github.com:greek314/acmev1.git

# Record credentials.
$ git config --global user.name "archimedes"
$ git config --global user.email "greek314@example.com"

# Add the contents of this folder to git and update the repository.
$ git add --all
$ git commit -m "initial commit"
$ git push origin main
```

If you enter the repository URL incorrectly in the `git remote add origin` step, you can reset it with the following line.
```bash
$ git remote set-url origin git@github.com:<username>/<repo>.git
```

6. _Download data files_.
Many labs have accompanying data files.
To download these files, navigate to your clone and run the `download_data.sh` bash script, which downloads the files and places them in the correct lab folder for you.

```bash
# Navigate to your folder and run the script.
$ cd /path/to/folder
$ bash download_data.sh
```

You can also find individual data files through [Student-Materials/wiki/Lab-Index](https://github.com/Foundations-of-Applied-Mathematics/Student-Materials/wiki/Lab-Index).

7. _Install Python package dependencies_.
If you use a Mac, you must have Brew installed.
To install the correct version of Python along with all necessary dependencies, navigate into your clone and run
```bash
$ bash install_python.sh
```
Now restart your terminal.
On Windows or Linux, you will need to run the following commands:
```bash
$ sudo apt-get install graphviz
$ sudo apt-get install libopenmpi-dev
$ sudo apt-get install ffmpeg
$ sudo apt-get install g++
$ sudo apt-get install python3-tk
$ sudo apt-get install openjdk-8-jdk
```
Assuming no errors, you should now run
```bash
$ bash install_dependencies.sh
```

8. (Optional) _Clone your repository_.
If you want your repository on another computer after completing steps 1-5, use the following commands.

```bash
# Navigate to where you want to put the folder.
$ cd ~/Desktop/or/something/

# Clone the folder from the online repository.
$ git clone git@github.com:<username>/<repo>.git <foldername>

# Record your credentials.
$ git config --global user.name "your name"
$ git config --global user.email "your email"

# Download data files to the new folder.
$ bash download_data.sh
```

# Using Git

Git manages the history of a file system through _commits_, or checkpoints.
Use `git status` to see the files that have been changed since the last commit.
These changes are then moved to the _staging area_, a list of files to save during the next commit, with `git add <filename(s)>`.
Save the changes in the staging area with `git commit -m "<A brief message describing the changes>"`.

All of these commands are done within a clone of the repository, stored somewhere on a computer.
This repository must be manually synchronized with the online repository via two other git commands: `git pull origin main`, to pull updates from the web to the computer; and `git push origin main`, to push updates from the computer to the web.

### Common Git Commands

| Command | Explanation |
|:--------|:------------|
| `git status` | Display the staging area and untracked changes. |
| `git pull origin main` | Pull changes from the online repository. |
| `git push origin main` | Push changes to the online repository. |
| `git add <filename(s)>` | Add a file or files to the staging area. |
| `git add -u` | Add all modified, tracked files to the staging area. |
| `git commit -m "<message>"` | Save the changes in the staging area with a given message. |
| `git checkout -- <filename>` | Revert changes to an unstaged file since the last commit. |
| `git reset HEAD -- <filename>` | Remove a file from the staging area. |
| `git diff <filename>` | See the changes to an unstaged file since the last commit. |
| `git diff --cached <filename>` | See the changes to a staged file since the last commit. |
| `git config --local <option>` | Record your credentials (`user.name`, `user.email`, etc.). |

**_NOTE_**: When pulling updates with `git pull origin main`, your terminal may sometimes display the following message.
```bash
Merge branch 'main' of https://github.com/<username>/<repo> into main

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
To close this screen and create the merge commit, type `:wq` and press `Enter`.

### Example Work Session

Short version:
```bash
$ cd ~/Desktop/Student-Materials/
$ git pull origin main                             # Pull updates.

# Make changes to a file.

# Record the changes in git.
$ git add -u                                       # Track changes.
$ git commit -m "Made some changes."               # Commit changes.
$ git push origin main                             # Push updates.
```

Long version:
```bash
# Navigate to the clone of the repository.
$ cd ~/Desktop/Student-Materials/

# Pull any updates from the online repository (such as TA feedback).
$ git pull origin main
From https://github.com/username/repo
 * branch            main     -> FETCH_HEAD
Already up-to-date.

# Work on the labs. For example, modify PythonIntro/python_intro.py.

$ git status
On branch main
Your branch is up-to-date with 'origin/main'.
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git checkout -- <file>..." to discard changes in working directory)

    PythonIntro/python_intro.py

# Track the changes with git.
$ git add PythonIntro/python_intro.py
$ git status
On branch main
Your branch is up-to-date with 'origin/main'.
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

    modified:   PythonIntro/python_intro.py

# Commit the changes to the repository with an informative message.
$ git commit -m "Made some changes"
[main fed9b34] Made some changes
 1 file changed, 10 insertion(+) 1 deletion(-)

# Push the changes to the online repository.
$ git push origin main
Counting objects: 3, done.
Delta compression using up to 2 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 327 bytes | 0 bytes/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://username@github.com/username/repo.git
   5742a1b..fed9b34  main -> main

# The changes have been saved and the online repository updated.
$ git status
On branch main
Your branch is up-to-date with 'origin/main'.
nothing to commit, working directory clean
```
