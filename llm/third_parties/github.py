import time
import os
import requests
import json
from dotenv import load_dotenv

load_dotenv()

class GithubAPI:

    def __init__(self, user) -> None:
        self.user: str = user
        self.headers: dict = {
            "Accept": "application/vnd.github+json",
            "Authorization": "Bearer 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",
            "X-GitHub-Api-Version": "2022-11-28"
        }

    def get_user(self):
        url = f"https://api.github.com/users/{self.user}"
        req = requests.get(url=url, headers=self.headers)

        res = json.loads(req.content)
        data = {
            "name":res.get("name", ""),
            "location":res.get("location", ""),
            "bio":res.get("bio", ""),
            "company":res.get("company", ""),
            "hireable":res.get("hireable", ""),
            "public_repos":res.get("public_repos", ""),
            "total_private_repos":res.get("total_private_repos", "")
        }
        return data

    def get_repos(self):
        url = f"https://api.github.com/users/{self.user}/repos"
        req = requests.get(url=url, headers=self.headers)
        return req
    
    


if __name__ == '__main__':
    user = "AlifvianM"
    req_us = GithubAPI(user=user).get_user()
    time.sleep(3)
    print(req_us)