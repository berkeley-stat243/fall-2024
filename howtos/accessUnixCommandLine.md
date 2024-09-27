---
title: Accessing the Unix Command Line
---

You have several options for UNIX command-line access. You'll need to choose one
of these and get it working.

### Mac OS (on your personal machine):

Open a Terminal by going to Applications -> Utilities -> Terminal

### Windows (on your personal machine):

1.  You may be able to use the Ubuntu bash shell available in Windows.

    Your PC must be running a 64-bit version of Windows 10 Anniversary Update or later (build 1607+).

    Please see this link for more information:

    - [https://msdn.microsoft.com/en-us/commandline/wsl/install_guide](https://msdn.microsoft.com/en-us/commandline/wsl/install_guide)
    
    For more detailed instructions, see the [Installing the Linux Subsystem on Windows](./windowsAndLinux.md) tutorial.

2. (Not recommended) There's an older program called cygwin that provides a UNIX command-line interface.

Note that when you install Git on Windows, you will get Git Bash. While you can
use this to control Git, the functionality is limited so this will not be enough
for general UNIX command-line access for the course.

### Linux (on your personal machine):

If you have access to a Linux machine, you very likely know how to access a terminal.

### Access via DataHub (provided by UC Berkeley's Data Science Education Program)

1) Go to [https://datahub.berkeley.edu](https://datahub.berkeley.edu)
2) Click on `Log in to continue`, sign in via CalNet, and authorize DataHub to have access to your account.
3) In the upper left, click on `File`, `New` and `Terminal`.
4) To end your session, click on `File`, `Hub Control Panel` and `Stop My Server`. Note that `Logout` will not end your running session, it will just log you out of it.

**While using DataHub for the bash unit (Unit 2) should be fine, if you try to use it for any problems sets or other work in class, you are likely to run out of memory.** The SCF JupyterHub (see below) should be used instead if you want browser-based access to a Linux environment, including the bash shell.

### Access via the Statistical Computing Facility (SCF)

With an SCF account (available [here](https://scf.berkeley.edu/account)), you can access a bash shell in the ways listed below. 

Those of you in the Statistics Department should be in the process of getting an SCF account. Everyone else will need an SCF account when we get to the unit on parallel computing, but you can request an account now if you prefer.

1. You can login to our various Linux servers and access a bash shell that way. Please see [http://statistics.berkeley.edu/computing/access](http://statistics.berkeley.edu/computing/access).

2. You can also access a bash shell via the SCF JupyterHub interface; please see the [Accessing Python](accessPython.md) instructions but when you click on `New`, choose `Terminal`. This is very similar to the DataHub functionality discussed above. 

