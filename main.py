import requests

from config import access_token
from utils import show_error_and_exit

print("Welcome to Make It Open Source")

repo_name = None
while not repo_name:
    repo_name = input('Please enter repository name : ')

repo_description = input('Enter repository description(optional) : ')

repo_info = {'name': repo_name, 'description': repo_description}
url = "https://api.github.com/user/repos?access_token=" + access_token

response = None
try:
    response = requests.post(url, json=repo_info)
    if response.status_code != 201:
        show_error_and_exit(response.text)
except requests.exceptions.RequestException as e:
    show_error_and_exit(e)

response_json = response.json()
print(response_json["name"] + " created successfully")
init_git = input('Init git project & connect to remote (y or n)?')
if init_git.strip().lower() == "y":
    clone_url = response_json['clone_url']
    print(clone_url)

print("Thank You !")
