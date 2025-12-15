# Make It Open Source

Quickly create a public repository on GitHub with just one command while starting a project.

### Setup Guide

1. Clone the **_MakeItOpenSource_** project.
2. Rename `config.example.py` to `config.py`
3. Obtain a personal access token for your GitHub account.  
   [Creating a Personal Access Token for the Command Line](https://help.github.com/en/articles/creating-a-personal-access-token-for-the-command-line)
4. Add your access token to `config.py`

### Usage Guide

1. Open the terminal and navigate to your project directory (the one you want to make open source).
2. Run the Python script `main.py` with the command:  
   `python FULL_PATH_TO_MAKE_IT_OPEN_SOURCE/main.py`
3. Provide the repository name (the project folder name is the default), repository description (optional), and confirmation to initialize and add remote.
4. Use the 'q' argument for quick repository setup with default values(repo name = folder name, no description):  
   `python FULL_PATH_TO_MAKE_IT_OPEN_SOURCE/main.py q`

### Setup Alias for Easy Use

For **Ubuntu** or **MacOS** (on .zshrc or .bashrc):

*If using Zsh shell (.zshrc)*.  
```bash
alias mios="python /path/to/MakeItOpenSource/main.py"
```

*If using Bash shell (.bashrc)*.  
```bash
alias mios="python /path/to/MakeItOpenSource/main.py"
```

For **Windows**, you need to setup Environment Variable.

Now you can simply use `mios` or `mios q` for quick repository setup.

<hr/>

Please let me know if you have any queries, feedback, or suggestions.
