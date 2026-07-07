..  Copyright (C)  Dave Parillo.  Permission is granted to copy, distribute
    and/or modify this document under the terms of the GNU Free Documentation
    License, Version 1.3 or any later version published by the Free Software
    Foundation; with Invariant Sections being Forward, and Preface,
    no Front-Cover Texts, and no Back-Cover Texts.  A copy of
    the license is included in the section entitled "GNU Free Documentation
    License".

.. index:: 
   single: git setup; GitHub

Git setup
=========
All of the assignments in this course are turned in
using a source code change management tool called ``git``.
`Git <https://git-scm.com>`__ is a distributed version-control system
for tracking changes in source code during software development.
It is designed for coordinating work among programmers,
but it can be used to track changes in any set of files.
If you continue working as a programmer, even if your team
doe not use git, it most certainly will use a tool with similar capabilities.

To use Git on the command line, you'll need to download, install, 
and configure Git on your computer. 

.. note::

   You will not be able to turn in any assignments until
   **all three** steps have been completed.

Step 1: Install Git
-------------------
Download and install the version of git appropriate for your operating system
from the  `git download site <https://git-scm.com/downloads>`__.
You may down load the GUI if you like, however, all of the examples
in this text will be on the command line.

If you are only using the Mesa server, you can skip this step.
Git has been installed for you.

Step 2: Setup your username and email address in Git
----------------------------------------------------
Git uses a username to associate commits with an identity.
The Git username is not the same as your GitHub username.
In this class, you should use the name you used to register for this course.

#. Open a terminal or Git Bash
#. Set your Git user name for all repositories on this computer:
   
   .. code-block:: none

      git config --global user.name "Mona Lisa"

#. Confirm your Git user name is set correctly:
   
   .. code-block:: none

      git config --global user.name

   which should display in this case:

   .. code-block:: none

      Mona Lisa

GitHub uses your commit email address to associate commits with your GitHub account.
You can choose the email address that will be associated with the commits you 
push from the command line as well as web-based Git operations you make.

#. Open a terminal or Git Bash
#. Set your Git email address for all repositories on this computer:

   .. code-block:: none

      git config --global user.email "email@example.com"

#. Confirm your Git user email is set correctly:
   
   .. code-block:: none

      git config --global user.email

   which should display in this case:

   .. code-block:: none

      email@example.com

If you want to receive email when I create issues or comment on your code,
then you should use a valid email address.

If you want to keep your email address private, you can do this on GitHub.
For more information see the 
`Manaing email page <https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address>`__
on GitHub.

Step 3: Setup authentication
----------------------------
When you connect to a GitHub repository from Git,
you'll need to authenticate with GitHub using either HTTPS or SSH.

Starting in 13 August 2021, basic authentication using a password to Git 
no longer works.
GitHub requires the use of token-based authentication
(for example, a personal access token, or an SSH key)
for all authenticated Git operations.
See `this blog post <https://github.blog/security/application-security/token-authentication-requirements-for-git-operations/>`__
for details.

Although GitHub provides many authentication choices, 
in this class you will need to be able to access
GitHub from the Mesa server.
This means you need to use either a personal access token or SSH.

You do not need to create both, but you are free to do so.

- A personal access token only works when
  performing Git operations over HTTPS.

- An SSH key only works when
  performing Git operations over SSH.

Creating an SSH key
...................
You can connect to GitHub using the Secure Shell Protocol (SSH), 
which provides a secure channel over an unsecured network.

Using the SSH protocol,
you can connect and authenticate to remote servers and services.
With SSH keys,
you can connect to GitHub without supplying your username and 
personal access token at each visit.

.. note::

   As a security precaution,
   GitHub automatically removes your inactive SSH keys
   that have not been used for a year.
   For more information, see 
   "`Deleted or missing SSH keys <https://docs.github.com/en/authentication/troubleshooting-ssh/deleted-or-missing-ssh-keys>`__."


If you don't already have an SSH key,
then you must generate a new SSH key to use for authentication.
If you're unsure whether you already have an SSH key, 
then you can check for existing keys.
For more information, see "`Checking for existing SSH keys <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys>`__."

To create an SSH key do the following:

#. Login to the Mesa server or open a local terminal or Git Bash shell
#. Paste the text below, substituting in your GitHub email address:

   .. code-block:: none

      ssh-keygen -t ed25519 -C "your_email@example.com"


   This creates a new ssh key, using the provided email as a label.
   You should see:

   .. code-block:: none

      Generating public/private ed25519 key pair.


#. When you're prompted to "Enter a file in which to save the key,"
   press Enter. This accepts the default file location.

   .. code-block:: none

      Enter file in which to save the key (/home/students/fire/fire40/.ssh/id_ed25519):

   You should see:

   .. code-block:: none

      Created directory '/home/students/fire/fire40/.ssh'.

#. At the prompt, type a secure passphrase. 
   For more information, see 
   "`Working with SSH key passphrases <https://docs.github.com/en/authentication/connecting-to-github-with-ssh/working-with-ssh-key-passphrases>`__."

   .. code-block:: none

      Enter passphrase (empty for no passphrase): [Type a passphrase]
      Enter same passphrase again: [Type passphrase again]


   You will see some other output, but most important is the file containing
   your public key, which will be similar to:

   .. code-block:: none

      Your public key has been saved in /var2/home/fire/fire40/.ssh/id_ed25519.pub.

   Make note of that, as you'll need it in the next steps.

To configure your GitHub account to use your SSH key,
you'll also need to add it to your GitHub account.

#. First, copy your public SSH key.

   .. code-block:: none

      cat ~/.ssh/id_ed25519.pub

   This command will display the contents of your public key
   which you can then copy and paste in the browser.
   The ``~`` is just an alias for your home directory.

   .. caution:: **Private keys are sensitive data!**

      Treat your private keys like passwords and keep them secret. 

      Your private key is stored in a separate file -  by default
      it is the same file name as your public key without the ".pub"
      file extension.

      Never post your private key on a web page or any other public location
      even for a short time.

      If you think your private key has been compromised, you should delete
      it and create a new one.


#. In the upper-right corner of any page on GitHub, click your profile photo, 
   then click **Settings**.
#. In the user settings sidebar, click **SSH and GPG keys**.
#. Click **New SSH key** or **Add SSH key**.
#. In the "Title" field, add a descriptive label for the new key.
   For example, if you created this on the Mesa server, 
   you might call this key "Mesa College CISC187".
#. Paste your key into the "Key" field.
#. Click **Add SSH key**.
#. If prompted, confirm your **GitHub password**.

Now you are ready to use your SSH key.



Using an SSH key on the command line
....................................
After you've set up your SSH key and added it to your GitHub account,
you can use it.
Since the setup is more complicated than a simple token,
it's a good idea to test it first.
When you test your connection,
you'll need to authenticate using your SSH key passphrase you created earlier. 

Test your SSH keys:

#. Login to the Mesa server (or other location of you public/private SSH key pair)
#. Enter the following:

   .. code-block:: none

      ssh -T git@github.com

   This will attempt to connect to github.com over ssh.

   You may see a warning like this:

   .. code-block:: none

      The authenticity of host 'github.com (IP ADDRESS)' can't be established.
      RSA key fingerprint is SHA256:nThbg6kXUpJWGl7E1IGOCspRomTxdCARLviKw6E5SY8.
      Are you sure you want to continue connecting (yes/no)?


#. Verify that the fingerprint in the message you see matches 
   `GitHub's RSA public key fingerprint <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/githubs-ssh-key-fingerprints>`__.
   If it does, then type yes:

   .. code-block:: none

      Hi username! You've successfully authenticated, but GitHub does not
      provide shell access.

#. Verify that the resulting message contains your username.
   If you receive a "permission denied" message, see
   "`Error: Permission denied (publickey) <https://docs.github.com/en/authentication/troubleshooting-ssh/error-permission-denied-publickey>`__".


A common source of error is using your GitHub username over SSH.

.. note:: Always use the "git" user

   All connections, including those for remote URLs, 
   must be made as the "git" user.
   If you try to connect with your GitHub username:

   .. code-block:: none

      ssh -T GITHUB-USERNAME@github.com

   then it will fail:

   .. code-block:: none

      Permission denied (publickey).

Once your SSH key is setup correctly, the only real difference in using it is
the URL you use to clone a repository.
To clone using SSH use the following command:

.. code-block:: none

   git clone git@github.com:DaveParillo/cisc187-TTYY-fireNN.git

In the above URL, replace **TT** with either

- **sp** in the spring term
- **fa** in the fall term

and replace **YY** with the 2 digit year of the semester
and replace **NN** with your 2 digit fire number assigned to you.

For example:

.. code-block:: none

   git clone git@github.com:DaveParillo/cisc187-sp21-fire01.git


Creating a GitHub personal access token
.......................................
Personal access tokens (PATs) are an alternative to using passwords for
authentication to GitHub when using the git command line.

.. note::

   As a security precaution,
   GitHub automatically removes personal access tokens that
   haven't been used in a year.

Follow the instructions on
`GitHub <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens>`__
to create a personal access token

At a minimum, you will want to ensure you give the token access to repositories
from the command line.
At the "scopes" or "permissions" screen, ensure you have **repo** selected.

After you have copied your token and leave the token creation page,
you will not be able to see it again.

.. caution:: **Tokens are sensitive data!**

   Treat your tokens like passwords and keep them secret. 

   A PAT is not your password, but it provides access to your source code.

   If you think your token has been compromised, delete it on GitHub
   and make a new token.


Using a token on the command line
.................................
Once you have a token, you can enter it instead of your password when
performing Git operations over HTTPS.

For example, to get a copy of all your assignments
on the command line you would enter the following:

.. code-block:: none

   git clone https://github.com/DaveParillo/cisc187-TTYY-fireNN.git
   Username: your_username
   Password: your_token

In the above URL, replace **TT** with either

- **sp** in the spring term
- **fa** in the fall term

and replace **YY** with the 2 digit year of the semester
and replace **NN** with your 2 digit fire number assigned to you.

Do **not** enter your password at the prompt.
Yes, I know it says 'password'.
Enter your personal access token
Personal access tokens can only be used for HTTPS Git operations.

Instead of manually entering your PAT for every HTTPS Git operation, 
you can cache your PAT with a Git client.
Git will temporarily store your credentials in memory
until an expiry interval has passed. 
You can also store the token in a plain text file that Git 
can read before every request. 

For more information, see 
"`Caching your GitHub credentials in Git <https://docs.github.com/en/get-started/git-basics/caching-your-github-credentials-in-git>`__."

-----

.. admonition:: More to Explore

   - `Git Documentation <https://git-scm.com/doc>`__
   - `GitHub quickstart <https://docs.github.com/en/get-started/start-your-journey>`__
   - `Creating SSH Keys <https://docs.github.com/en/authentication/connecting-to-github-with-ssh>`__
   - `Creating a GitHub Personal Access Token <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens>`__



