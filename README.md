# Make It Open Source
Quickly create public repository in GitHub while creating a project.

Create a public GitHub repo, init git & add remote with single command.

**Setup guide**
1. Clone MakeItOpenSource project.
2. Rename config.example.py to config.py.
3. Get personal access token for your GitHub account.
https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line
4. Add your access token to config.py

**Usage guide**
1. Open terminal & navigate to your project (not MakeItOpenSource).
2. Run python script main.py from make it open source : *python FULL_PATH_TO_MAKE_IT_OPEN_SOURCE/main.py*
3. Provide repo name (project folder name is default), repo description (optional) and confirmation to init & add remote.
4. Use q argument for quick repo setup. *..../main.py q*

**Use alias for easy use**

Example for Ubuntu (on .bashrc)

*alias mios="python /home/...../Projects/Python/MakeItOpenSource/main.py"*

Now just *mios* or *mios q* will be enough.