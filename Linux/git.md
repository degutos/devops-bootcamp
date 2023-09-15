# GIT

Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency.

## Areas and sessions of GIT

- Working area
- Staging area
- Commited Files




## Installing Git

```
sarah@dev01:~$ sudo apt-get install git 
Reading package lists... Done
Building dependency tree       
Reading state information... Done
Suggested packages:
  gettext-base git-daemon-run | git-daemon-sysvinit git-doc git-el git-email git-gui gitk gitweb git-cvs git-mediawiki git-svn
The following NEW packages will be installed:
  git
0 upgraded, 1 newly installed, 0 to remove and 180 not upgraded.
Need to get 3990 kB of archives.
After this operation, 32.6 MB of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 git amd64 1:2.17.1-1ubuntu0.18 [3990 kB]
Fetched 3990 kB in 1s (7181 kB/s)
debconf: delaying package configuration, since apt-utils is not installed
Selecting previously unselected package git.
(Reading database ... 23634 files and directories currently installed.)
Preparing to unpack .../git_1%3a2.17.1-1ubuntu0.18_amd64.deb ...
Unpacking git (1:2.17.1-1ubuntu0.18) ...
Setting up git (1:2.17.1-1ubuntu0.18) ...
```



## Checking git version

```
sarah@dev01:~$ git --version
git version 2.17.1
```


## Git Help

```
sarah@dev01:~$ git help
usage: git [--version] [--help] [-C <path>] [-c <name>=<value>]
           [--exec-path[=<path>]] [--html-path] [--man-path] [--info-path]
           [-p | --paginate | --no-pager] [--no-replace-objects] [--bare]
           [--git-dir=<path>] [--work-tree=<path>] [--namespace=<name>]
           <command> [<args>]

These are common Git commands used in various situations:

start a working area (see also: git help tutorial)
   clone      Clone a repository into a new directory
   init       Create an empty Git repository or reinitialize an existing one

work on the current change (see also: git help everyday)
   add        Add file contents to the index
   mv         Move or rename a file, a directory, or a symlink
   reset      Reset current HEAD to the specified state
   rm         Remove files from the working tree and from the index

examine the history and state (see also: git help revisions)
   bisect     Use binary search to find the commit that introduced a bug
   grep       Print lines matching a pattern
   log        Show commit logs
   show       Show various types of objects
   status     Show the working tree status

grow, mark and tweak your common history
   branch     List, create, or delete branches
   checkout   Switch branches or restore working tree files
   commit     Record changes to the repository
   diff       Show changes between commits, commit and working tree, etc
   merge      Join two or more development histories together
   rebase     Reapply commits on top of another base tip
   tag        Create, list, delete or verify a tag object signed with GPG

collaborate (see also: git help workflows)
   fetch      Download objects and refs from another repository
   pull       Fetch from and integrate with another repository or a local branch
   push       Update remote refs along with associated objects

'git help -a' and 'git help -g' list available subcommands and some
concept guides. See 'git help <command>' or 'git help <concept>'
to read about a specific subcommand or concept.
```


## Installing git man pages

```
sarah@dev01:~$ sudo apt-get install git-man
Reading package lists... Done
Building dependency tree       
Reading state information... Done
The following packages will be upgraded:
  git-man
1 upgraded, 0 newly installed, 0 to remove and 179 not upgraded.
Need to get 804 kB of archives.
After this operation, 2048 B of additional disk space will be used.
Get:1 http://archive.ubuntu.com/ubuntu bionic-updates/main amd64 git-man all 1:2.17.1-1ubuntu0.18 [804 kB]
Fetched 804 kB in 0s (1785 kB/s)
debconf: delaying package configuration, since apt-utils is not installed
(Reading database ... 24358 files and directories currently installed.)
Preparing to unpack .../git-man_1%3a2.17.1-1ubuntu0.18_all.deb ...
Unpacking git-man (1:2.17.1-1ubuntu0.18) over (1:2.17.1-1ubuntu0.6) ...
Setting up git-man (1:2.17.1-1ubuntu0.18) ...
Processing triggers for man-db (2.8.3-2ubuntu0.1) ...
```

Example how to use it:

```
$ git help init
```


# Initializing a repositoy

```
$ git init
```

```
sarah $ git init
hint: Using 'master' as the name for the initial branch. This default branch name
hint: is subject to change. To configure the initial branch name to use in all
hint: of your new repositories, which will suppress this warning, call:
hint: 
hint:   git config --global init.defaultBranch <name>
hint: 
hint: Names commonly chosen instead of 'master' are 'main', 'trunk' and
hint: 'development'. The just-created branch can be renamed via this command:
hint: 
hint:   git branch -m <name>
Initialized empty Git repository in /home/sarah/story-blog/.git/
```

Let's confirm that git has created a `.git` folder 

```
sarah $ ls -la
total 12
drwxr-sr-x    3 sarah    sarah         4096 Aug  4 10:43 .
drwxr-sr-x    1 sarah    sarah         4096 Aug  4 10:42 ..
drwxr-sr-x    7 sarah    sarah         4096 Aug  4 10:43 .git
```



## Creating first file to our project

```
sarah $ echo "A Lion lay asleep in the forest" > lion-and-mouse.txt
sarah $ ls
lion-and-mouse.txt


sarah $ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        lion-and-mouse.txt

nothing added to commit but untracked files present (use "git add" to track)
```


# GIT log

Git log will show all commit log made

```
sarah (master)$ git log
commit 4d6431f521b1092aa8cec7838d5d89c58da4415a (HEAD -> master)
Author: sarah <sarah@example.com>
Date:   Fri Aug 4 11:02:43 2023 +0000

    Added the lion and mouse story
```

When there is no previously commit made we will see this msg

```
sarah $ git log
fatal: your current branch 'master' does not have any commits yet
```

### Show log with files changed name

To see the commit log and the file's name

```
sarah (master)$ git log --name-only
commit 4d6431f521b1092aa8cec7838d5d89c58da4415a (HEAD -> master)
Author: sarah <sarah@example.com>
Date:   Fri Aug 4 11:02:43 2023 +0000

    Added the lion and mouse story

lion-and-mouse.txt
```

### Show log in one line

```
sarah (master)$ git log --oneline
e30b881 (HEAD -> master) Added a new story
4d6431f Added the lion and mouse story
```

### Checking git status 

```
sarah (master)$ ls
README.md  assets     css        fonts      img        index.php  js         scss       vendors
```

#### When we have local commits to be pushed to remote git

```
sarah (master)$ git status
On branch master
Your branch is ahead of 'origin/master' by 3 commits.
  (use "git push" to publish your local commits)

nothing to commit, working tree clean
```


#### Git help

```
$ git help log
```


### Limiting to see only 3 last logs

```
sarah (master)$ git log -n 3
commit 02d0500b9df09c76350561988696f1449657f215 (HEAD -> master)
Author: tej <tej@example.com>
Date:   Fri Aug 4 10:59:36 2023 +0000

    Update color from red to green

commit ce43ee0007693306b40bb49794fc4ed616d4026a
Author: sarah <sarah@example.com>
Date:   Fri Aug 4 10:59:36 2023 +0000

    Add instructions to verify application

commit e4db2407693943e1a3e26464c712c9198964a7e2
Author: max <max@example.com>
Date:   Fri Aug 4 10:59:36 2023 +0000

    Increase interval time to 500
```


### Viewing 3 last commits in logs and showing files names

```
sarah (master)$ git log -n 3 --name-only
commit 02d0500b9df09c76350561988696f1449657f215 (HEAD -> master)
Author: tej <tej@example.com>
Date:   Fri Aug 4 10:59:36 2023 +0000

    Update color from red to green

css/style.css

commit ce43ee0007693306b40bb49794fc4ed616d4026a
Author: sarah <sarah@example.com>
Date:   Fri Aug 4 10:59:36 2023 +0000

    Add instructions to verify application

README.md

commit e4db2407693943e1a3e26464c712c9198964a7e2
Author: max <max@example.com>
Date:   Fri Aug 4 10:59:36 2023 +0000

    Increase interval time to 500

js/theme.js
```


# GIT Branch 


Branches allow you to work on different parts of a project without impacting the main branch. When the work is complete, a branch can be merged with the main project. You can even switch between branches and work on different projects without them interfering with each other.


### Branch commands

```
$ git branch # list all branches
$ git branch andre # create a new branch
$ git checkout andre # switch to branch andre
$ git checkout -b andre # create a new branch and switch to it
$ git branch -d andre # delete a branch
```


```
sarah (master)$ git checkout -b frogs-and-ox
Switched to a new branch 'frogs-and-ox'


sarah (frogs-and-ox)$ git branch
* frogs-and-ox
  master
```

#### Creating a branch sotry/frog-and-ox

```
sarah (master)$ git branch
* master


sarah (master)$ git checkout -b story/frogs-and-ox
Switched to a new branch 'story/frogs-and-ox'

sarah (story/frogs-and-ox)$ git branch
  master
* story/frogs-and-ox
```


Check log and check HEAD

```
sarah (story/frogs-and-ox)$ git log
commit 4561696e18cf7938f107fc65422902f84fd92ca9 (HEAD -> story/frogs-and-ox, master)
Author: sarah <sarah@example.com>
Date:   Fri Aug 4 11:51:22 2023 +0000

    Added the lion and mouse story
```


When we are working on a project and a branch and we have unfineshed work but we need change our branch to fix another issue in that branch we may stage the unfineshed work and commit first and then move to a new branch

```
sarah (story/frogs-and-ox)$ git status
On branch story/frogs-and-ox
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        frogs-and-ox.txt

nothing added to commit but untracked files present (use "git add" to track)
sarah (story/frogs-and-ox)$ git add frogs-and-ox.txt 
sarah (story/frogs-and-ox)$ git commit -m "Add incomplete frogs-and-ox story"
[story/frogs-and-ox 2fbc1c1] Add incomplete frogs-and-ox story
 1 file changed, 13 insertions(+)
 create mode 100644 frogs-and-ox.txt
sarah (story/frogs-and-ox)$ git status
On branch story/frogs-and-ox
nothing to commit, working tree clean
```

Then we can switch to a new branch

```
sarah (story/frogs-and-ox)$ git checkout master
Switched to branch 'master'
sarah (master)$ git branch
* master
  story/frogs-and-ox
```

Then we fix whatever we need to fix on that branch and commit

```
sarah (master)$ vi lion-and-mouse.txt 

sarah (master)$ git status
On branch master
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
        modified:   lion-and-mouse.txt

no changes added to commit (use "git add" and/or "git commit -a")

sarah (master)$ git add lion-and-mouse.txt 

sarah (master)$ git commit -m Fix "typo in story title"
error: pathspec 'typo in story title' did not match any file(s) known to git
sarah (master)$ git commit -m "Fix typo in story title"
[master f59aad7] Fix typo in story title
 1 file changed, 1 insertion(+), 1 deletion(-)


sarah (master)$ git status
On branch master
nothing to commit, working tree clean
```

Now we can switch back to other branc

```
sarah (master)$ git checkout story/frogs-and-ox
Switched to branch 'story/frogs-and-ox'
```

#### Listing all branches

```
sarah (master)$ git branch
  feature/cart
  feature/checkout
  feature/signout
  feature/signup
* master
```

### Checking what branch a branch was created from 

```
sarah (master)$ git checkout feature/signout
Switched to branch 'feature/signout'
sarah (feature/signout)$ git log --graph --decorate
* commit eb42d9985ef12f41ab9d06ad66d648f867369155 (HEAD -> feature/signout)
| Author: sarah <sarah@example.com>
| Date:   Fri Aug 4 11:51:21 2023 +0000
| 
|     Add signout page
| 
* commit c9686d96a0b512e37e0d37725b97b432373dc0cb (feature/signup)
| Author: sarah <sarah@example.com>
| Date:   Fri Aug 4 11:51:21 2023 +0000
| 
|     Add signup page
| 
* commit 619cc099ba944dffcee7c22baee6e1255c053076 (master)
  Author: sarah <sarah@example.com>
  Date:   Fri Aug 4 11:51:21 2023 +0000
  
      Added main page
```


### How to revert the last change

```
$ git reset --soft HEAD~1
```


#### Head

Head is the last commit made in the branch you are
When you usually switch to a new branch you usually reach the head of that branch



## Remote repository

We can have a remote repository to push our code to
Sample:
- github
- gitlab
- bitbucket

We will need a connection string to reach the remote address

```
$ git remote add origin htts://..../.../[name].git
```

we can use the above command with `origin` as an alias in order to not have to type the connection string every time


We can use the below command to list all the remote repository

```
$ git remote -v 
```


### Pushing

We can sync our local repo to remote repo

```
$ git push origin master
```

### Creating a remote repository

We can use Github, gitlab or bucket to create a new repository under our accout 
Once we create a new repository we are able to push our local code into it


#### Adding the local repository to reach the remote repo

```
sarah (master)$ git remote add origin http://git.example.com/sarah/story-blog.git
sarah (master)$ git remote -v
origin  http://git.example.com/sarah/story-blog.git (fetch)
origin  http://git.example.com/sarah/story-blog.git (push)
```


#### Pushing our local code into our remote repository

```
sarah (master)$ git push origin master
Username for 'http://git.example.com': sarah
Password for 'http://sarah@git.example.com': 
Enumerating objects: 14, done.
Counting objects: 100% (14/14), done.
Delta compression using up to 36 threads
Compressing objects: 100% (12/12), done.
Writing objects: 100% (14/14), 2.05 KiB | 2.05 MiB/s, done.
Total 14 (delta 4), reused 0 (delta 0), pack-reused 0
remote: . Processing 1 references
remote: Processed 1 references in total
To http://git.example.com/sarah/story-blog.git
 * [new branch]      master -> master
```

- After pushing our code to remote repository we wil be able to see it into our remote UI (github)
- The above command pushed the local code into the MASTER remote branch, we don't want people push their code directly into master branch. Let's do it the right way creating a Pull Request








### Pull Request

- We should not merge into Master branch directly
- We should always push or code to a new branch and then create a PR to merge from the branch to the master branch
- Some teammate should approve your PR and Merge


#### Cloning our repository into our Local computer

```
max $ git clone http://git.example.com/sarah/story-blog
Cloning into 'story-blog'...
remote: Enumerating objects: 14, done.
remote: Counting objects: 100% (14/14), done.
remote: Compressing objects: 100% (12/12), done.
remote: Total 14 (delta 4), reused 0 (delta 0), pack-reused 0
Receiving objects: 100% (14/14), done.
Resolving deltas: 100% (4/4), done.
```


#### Adding a new file called fox-and-grapes.txt

```
max (master)$ ls
fox-and-grapes.txt  lion-and-mouse.txt
frogs-and-ox.txt
max (master)$ git status
On branch master
Your branch is up to date with 'origin/master'.

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        fox-and-grapes.txt

nothing added to commit but untracked files present (use "git add" to track)
```


As we notice we have a new file called gox-and-grapes.txt and this file is untracked
We will need to create a new branch called story/fox-and-grapes and commit this file in there

```
max (master)$ git checkout -b story/fox-and-grapes
Switched to a new branch 'story/fox-and-grapes'
max (story/fox-and-grapes)$ 
max (story/fox-and-grapes)$ git status
On branch story/fox-and-grapes
Untracked files:
  (use "git add <file>..." to include in what will be committed)
        fox-and-grapes.txt

nothing added to commit but untracked files present (use "git add" to track)
```


#### Adding / tracking a file into new branch story/fox-and-grapes

```
max (story/fox-and-grapes)$ git add fox-and-grapes.txt 
max (story/fox-and-grapes)$ git commit -m "Added fox-and-grapes story"
[story/fox-and-grapes a97d441] Added fox-and-grapes story
 1 file changed, 21 insertions(+)
 create mode 100644 fox-and-grapes.txt
```

#### Pushing the local branch into new remote branch story/fox-and-grapes

```
max (story/fox-and-grapes)$ git push  origin story/fox-and-grapes
Username for 'http://git.example.com': max
Password for 'http://max@git.example.com': 
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 36 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 742 bytes | 742.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
remote: 
remote: Create a new pull request for 'story/fox-and-grapes':
remote:   http://git.example.com/sarah/story-blog/compare/master...story/fox-and-grapes
remote: 
remote: . Processing 1 references
remote: Processed 1 references in total
To http://git.example.com/sarah/story-blog
 * [new branch]      story/fox-and-grapes -> story/fox-and-grapes
```

- Now we can go to UI and see that new code was pushed into a new remote branch created 
- We can now create a new PR to merge story/fox-and-grapes into master branch
- We can also add reviewers to our new created PR 
- Login as another user in git and review and approve the PR
- Once the PR as merged we should see the change in Master branch





### Fetching and Pulling


When we push our code to a remote new branch and create a Pull request to merge the code from the new branch into the master branch all the manual process is made manually through the UI, that means our local repository doensn't know about this merge, we will need to inform our local repository (master branch) about that change.


In order to update our remote master branch into our local repo run the fetch command to fech the remote branch into local repo

```
$ git fetch origin master
```


Example:

```
sarah (master)$ git fetch origin master
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 724 bytes | 724.00 KiB/s, done.
From http://git.example.com/sarah/story-blog
 * branch            master     -> FETCH_HEAD
   d8a9d39..c5b2ec6  master     -> origin/master
```

To see all our branches, local and remote run:

```
sarah (master)$ git branch -a
* master
  story/frogs-and-ox
  remotes/origin/master
```


In order to merge our origin master into localhost we run 

```
$ git merge origin/master
```

Example:

```
sarah (master)$ git merge origin/master
Updating d8a9d39..c5b2ec6
Fast-forward
 fox-and-grapes.txt | 21 +++++++++++++++++++++
 1 file changed, 21 insertions(+)
 create mode 100644 fox-and-grapes.txt
```

We also can run the pull command instead of the two commands above

```
$ git pull origin master
```

Example:

```
sarah (master)$ git pull origin master
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 776 bytes | 776.00 KiB/s, done.
From http://git.example.com/sarah/story-blog
 * branch            master     -> FETCH_HEAD
   c5b2ec6..139810f  master     -> origin/master
Updating c5b2ec6..139810f
Fast-forward
 donkey-and-dog.txt | 19 +++++++++++++++++++
 1 file changed, 19 insertions(+)
 create mode 100644 donkey-and-dog.txt
```


### Merging conflicts

- Sometimes people add files and push code into the remote repo and you pull the code before pushing your code to Github. If not you will ge some error:


```
max (master)$ git push origin master
To http://git.example.com/sarah/story-blog.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'http://git.example.com/sarah/story-blog.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```


Now to fix this we need to pull remote into local 

```
max (master)$ git pull origin master
remote: Enumerating objects: 4, done.
remote: Counting objects: 100% (4/4), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 1), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 304 bytes | 304.00 KiB/s, done.
From http://git.example.com/sarah/story-blog
 * branch            master     -> FETCH_HEAD
   9f8f574..35d6daa  master     -> origin/master
hint: Pulling without specifying how to reconcile divergent branches is
hint: discouraged. You can squelch this message by running one of the following
hint: commands sometime before your next pull:
hint: 
hint:   git config pull.rebase false  # merge (the default strategy)
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
hint: 
hint: You can replace "git config" with "git config --global" to set a default
hint: preference for all repositories. You can also pass --rebase, --no-rebase,
hint: or --ff-only on the command line to override the configured default per
hint: invocation.
CONFLICT (add/add): Merge conflict in story-index.txt
Auto-merging story-index.txt
Automatic merge failed; fix conflicts and then commit the result.
```

The problem is our local repo has the same file in remote repo, when we pull the remote code to local the file story-index.txt is conflitant and will be saved with both content (merged)

Last log can show us that the file was added before

```
max (master)$ git log | head -n 5
commit b0cf26d945e879b5ed9f6f1595c40eed013a3c64
Author: max <max@example.com>
Date:   Fri Sep 15 09:13:25 2023 +0000

    Add index of stories
```


Lets see the conflict 

```
max (master)$ cat story-index.txt 
<<<<<<< HEAD
1. The Lion and the Mooose
2. The Frogs and the Ox
3. The Fox and the Grapes
4. The Donkey and the Dog
=======
1. The Lion and the Mouse
2. The Frogs and the Ox
3. The Fox and the Grapes
>>>>>>> 35d6daa2088b92d95d2dae9f6ba96fa39ec3832d
```

- Now we should edit the file above and fix the change manually. After that save the file and commit the fix


```
max (master)$ cat story-index.txt 
1. The Lion and the Mouse
2. The Frogs and the Ox
3. The Fox and the Grapes
4. The Donkey and the Dog
```

```
max (master)$ git add story-index.txt 
max (master)$ git commit -m "Resolved merge conflicts and merged story index"
[master 92456dd] Resolved merge conflicts and merged story index
```


- Now we push the fix to github

```
max (master)$ git push origin master
Enumerating objects: 9, done.
Counting objects: 100% (9/9), done.
Delta compression using up to 36 threads
Compressing objects: 100% (6/6), done.
Writing objects: 100% (6/6), 626 bytes | 626.00 KiB/s, done.
Total 6 (delta 3), reused 0 (delta 0), pack-reused 0
remote: . Processing 1 references
remote: Processed 1 references in total
To http://git.example.com/sarah/story-blog.git
   35d6daa..92456dd  master -> master
```



### Fork

- We can fork a project into our repository and change it as we wish. All we will need is a read access to the original repository
- I user can fork a project, change it and sent a new PR to the original project to approve or not the change 
- We can use the UI to fork any project we want since we have read access
- After forking we can clone it into our local computer, change it and push the change to remote forked project
- After that we can create a PR from our forked project into the original project and wait for review and approval to our code into the original repository 



