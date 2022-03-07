import requests

from github import Github
from misc import read_token


def get_release_file(filename: str, repo: str, prerelease: bool = False):
    """Download from Github the latest release files"""
    g = Github(read_token())
    repository = g.get_repo(repo)
    all_releases = repository.get_releases()
    assets_release = None

    for release in all_releases:
        print(f'Get "{filename}", with a prerelease value to "{prerelease}" ')
        if release.prerelease is prerelease:
            assets_release = release.get_assets()
            break
        else:
            assets_release = release.get_assets()
            break

    for file in assets_release:
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
