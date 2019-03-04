import os
import sys

import requests

from config import access_token
from utils import show_error_and_exit

print("Welcome to Make It Open Source")

quick = len(sys.argv) > 1 and sys.argv[1].strip().lower() == "q"

folder = os.path.basename(os.getcwd())
if quick:
    repo_name = folder
    repo_description = ""
else:
    repo_name = input("Please enter repository name (default " + folder + "): ")
    repo_name = folder if not repo_name else repo_name
    repo_description = input('Enter repository description (optional) : ')

repo_info = {'name': repo_name, 'description': repo_description}
url = "https://api.github.com/user/repos?access_token=" + access_token

response = None
try:
    print("Creating repo for " + repo_name)
    response = requests.post(url, json=repo_info)
    if response.status_code != 201:
        show_error_and_exit(response.text)
except requests.exceptions.RequestException as e:
    show_error_and_exit(e)

response_json = response.json()
print(response_json["name"] + " created successfully.")

init_git = None
if not quick:
    init_git = input('Init git project & connect to remote (y or n)?')
if quick or init_git.strip().lower() == "y":
    clone_url = response_json['clone_url']
    os.system("git init")
    os.system("git remote add origin " + clone_url)

print("Thank You !")
