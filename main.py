import requests
from utils import show_error_and_exit

print("Welcome to Make It Open Source")

repo_name = None
while not repo_name:
    repo_name = input('Please enter repository name : ')

repo_description = input('Enter repository description(optional) : ')

repo_info = {'name': repo_name, 'description': repo_description}
url = "https://api.github.com/users/repos?access_token=<generated token>"

try:
    response = requests.post(url, repo_info)
    if response.status_code != 200:
        show_error_and_exit(response.text)
except requests.exceptions.RequestException as e:
    show_error_and_exit(e)

print(response)
init_git = input('Init git project & connect to remote (y or n)?')
if init_git.strip().lower() == "y":
    print("Init Git")

print("Thank You !")
