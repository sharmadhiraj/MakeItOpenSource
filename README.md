# Make It Open Source
Quickly create public repository in GitHub while creating a project.

With this tool you can create a public GitHub repo, init git & add remote with single command.

**Setup guide**
1. Clone **_MakeItOpenSource_** project.
2. Rename _config.example.py_ to _config.py_.
3. Get personal _access token_ for your GitHub account.  
https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line
4. Add your _access token_ to _config.py_

**Usage guide**
1. Open terminal & navigate to your project (that you want to make open source).
2. Run python script _main.py_  
`python FULL_PATH_TO_MAKE_IT_OPEN_SOURCE/main.py`
3. Provide repo name (project folder name is default), repo description (optional) and confirmation to init & add remote.
4. Use q argument for quick repo setup with default values
`python FULL_PATH_TO_MAKE_IT_OPEN_SOURCE/main.py q`

**Setup alias for easy use**

For Ubuntu (on .bashrc)

`alias mios="python /home/...../Projects/Python/MakeItOpenSource/main.py"`

Now just `mios` or `mios q` will be enough.