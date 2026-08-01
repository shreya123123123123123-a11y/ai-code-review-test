import os
import requests
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("GITHUB_TOKEN")


headers = {
    "Authorization": f"token {TOKEN}"
}


def get_pull_request_files(repo, pr_number):

    url = f"https://api.github.com/repos/{repo}/pulls/{pr_number}/files"

    response = requests.get(
        url,
        headers=headers
    )

    return response.json()