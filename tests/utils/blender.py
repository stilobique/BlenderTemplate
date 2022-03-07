import json
import os

from pathlib import Path
from .forge import get_release_file


def get_b3d_addon_dependency(archive: list):
    """From json resources, get all blender dependency and download-it"""
    dependency = Path(os.getcwd(), "tests", "dependency.json")
    with open(dependency) as f:
        data = json.load(f)

    b3d_dependency = data['blender']
    for key, value in b3d_dependency.items():
        if 'prerelease' in value:
            prerelease = True
        else:
            prerelease = False
        get_release_file(value[0], value[1], prerelease=prerelease)
        archive.append(value[0])
