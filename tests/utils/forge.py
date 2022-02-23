import os
import requests

from pathlib import Path
from github import Github


def read_token():
    token_file = Path(os.getcwd(), 'tests', 'token.txt')
    with open(token_file, 'r') as f:
        token = f.read()

    return token


def get_release_file(filename: str, repo: str):
    g = Github(read_token())
    repository = g.get_repo(repo)
    latest = repository.get_latest_release()
    latest.get_assets()
    for file in latest.get_assets():
        if file.name == filename:
            dl_file(file.url, file.name)


def dl_file(url: str, filename: str):
    """From specific asset, download it"""
    headers = {
        'Authorization': f'token {read_token()}',
        'Accept': 'application/octet-stream'
    }
    session = requests.Session()
    link = session.get(url, stream=True, headers=headers)
    with open(filename, 'wb') as f:
        for chunk in link.iter_content(1024*1024):
            f.write(chunk)
