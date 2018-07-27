This repository contains specifications files for the Foundations of Applied Mathematics labs.
Skip down to [Section 2](#setup) for setup instructions.

The labs in this curriculum aim to introduce computational and mathematical concepts, walk through implementations of those concepts in Python, and use industrial-grade code to solve interesting, relevant problems.
Lab assignments are usually about 5-10 pages long and include code examples (yellow boxes), important notes (green boxes), warnings about common errors (red boxes), and about 3-7 exercises (blue boxes).
The lab manuals can be downloaded from [foundations-of-applied-mathematics.github.io](http://foundations-of-applied-mathematics.github.io/).

# Submitting Assignments

### Labs

Every lab has a corresponding specifications file with some code to get you started and to make your submission compatible with automated test drivers.
These materials are also hosted at [foundations-of-applied-mathematics.github.io](http://foundations-of-applied-mathematics.github.io/).
To get started, download the `zip` file for your class, unzip the folder, and move it somewhere where it won't get lost.
This folder has some setup scripts and a collection of folders, one per lab, each of which contains the specifications file(s) for that lab.
See [Student-Materials/wiki/Lab-Index](https://github.com/Foundations-of-Applied-Mathematics/Student-Materials/wiki/Lab-Index) for the complete list of labs, their specifications and data files, and the lab manual that each lab belongs to.

**_WARNING:_** do **not** move or rename the lab folders or the enclosed specifications files; if you do, the test drivers will not be able to find your assignment.
Make sure your folder and file names match [Student-Materials/wiki/Lab-Index](https://github.com/Foundations-of-Applied-Mathematics/Student-Materials/wiki/Lab-Index).

Labs are submitted via git.
To submit a lab, modify the provided specifications file and add, commit, and push the changes (see [Section 3](#using-git) for details on using git).
The instructor will drop feedback files in the lab folder after grading the assignment.
For example, the _Introduction to Python_ lab has `PythonIntro/python_intro.py` as its specifications file.
To complete that assignment, modify `PythonIntro/python_intro.py` and track the changes in git.
After grading, the instructor will create a file called `PythonIntro/PythonIntro_feedback.txt` with your score and some feedback.

### Homework

Non-lab coding homework should be placed in the `_Homework/` folder and submitted via git.
Be careful to name your assignment correctly so the instructor (and test driver) can find it.
The instructor may drop specifications files and/or feedback files in this folder as well.

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
If you use an academic email address (ending in `.edu`, etc.), you will get free unlimited public and private repositories.

2. _Make a new repository_.
On the Bitbucket page, click the **+** button from the menu on the left and, under **CREATE**, select **Repository**.
Provide a name for the repository, mark the repository as **private**, and make sure the repository type is **Git**.
Under **Advanced settings**, enter a short description for your repository, select **No forks** under forking, and select **Python** as the language.
Finally, click the blue **Create repository** button.
Take note of the URL of the webpage that is created; it should be something like `https://bitbucket.org/<username>/<repo>`.

3. _Give the instructor access to your repository_.
On your new Bitbucket repository page (`https://bitbucket.org/<username>/<repo>` or similar), go to **Settings** in the menu to the left and select **User and group access**, the second option from the top.
Enter your instructor's Bitbucket username under **Users** and click **Add**.
Select the blue **Write** button so your instructor can read from and write feedback to your repository.

4. _Connect your folder to the new repository_.
In a shell application (Terminal on Linux or Mac, or [Git Bash](http://git-scm.com/downloads) on Windows), enter the following commands.

```bash
# Navigate to your folder.
$ cd /path/to/folder        # cd means 'change directory'.

# Make sure you are in the right place.
$ pwd                       # pwd means 'print working directory'.
/path/to/folder
$ ls *.md                   # ls means 'list files'.
README.md                   # This means README.md is in the working directory.

# Connect this folder to the online repository.
$ git init
$ git remote add origin https://<username>@bitbucket.org/<username>/<repo>.git

# Record your credentials.
$ git config --local user.name "your name"
$ git config --local user.email "your email"

# Add the contents of this folder to git and update the repository.
$ git add --all
$ git commit -m "initial commit"
$ git push origin master
```

For example, if your Bitbucket username is `mathguy314`, the repository is called `pythonessentials`, and the folder is called `Python-Essentials-Student-Materials/` and is on the desktop, enter the following commands.

```bash
$ cd ~/Desktop/Python-Essentials-Student-Materials          # Navigate to the folder.
$ pwd                                                       # Make sure you are in the right place.
/Users/Me/Desktop/Python-Essentials-Student-Materials
$ ls *.md
README.md
$ git init                                                  # Connect this folder to the repository.
$ git remote add origin https://mathguy314@bitbucket.org/mathguy314/pythonessentials.git
$ git config --local user.name "archimedes"                 # Record your credentials.
$ git config --local user.email "mathguy314@example.com"
$ git add --all                                             # Add the contents of this folder to git.
$ git commit -m "initial commit"
$ git push origin master                                    # Update the repository.
```

If you enter the repository URL incorrectly in the `git remote add origin` step, you can reset it with the following line.
```bash
$ git remote set-url origin https://<username>@bitbucket.org/<username>/<repo>.git
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

6. (Optional) _Clone your repository_.
If you want your repository on another computer after completing steps 1-4, use the following commands.

```bash
# Clone the folder from the online repository.
$ cd ~/Desktop              # Navigate to where you want to put the folder.
$ git clone https://<username>@bitbucket.org/<username>/<repo>.git <foldername>

# Record your credentials in the new folder.
$ cd <foldername>
$ git config --local user.name "your name"
$ git config --local user.email "your email"
```
Repeat step 5 in this clone as well.

# Using Git

Git manages the history of a file system through _commits_, or checkpoints.
Use `git status` to see the files that have been changed since the last commit.
These changes are then moved to the _staging area_, a list of files to save during the next commit, with `git add <filename(s)>`.
Save the changes in the staging area with `git commit -m "<A brief message describing the changes>"`.

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
$ cd ~/Desktop/Python-Essentials-Student-Materials/
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
$ cd ~/Desktop/Python-Essentials-Student-Materials/

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
