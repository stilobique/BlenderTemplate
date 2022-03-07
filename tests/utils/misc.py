import os
import pathlib
import sys
import zipfile

from .issue import ArchiveFolderSourceNotFound
from pathlib import Path


def read_token(file: str = 'token.txt') -> str:
    """From tests folder, return a token string, in a dedicated file"""
    token_file = Path(os.getcwd(), 'tests', file)
    with open(token_file, 'r') as f:
        token = f.read()

    return token


def generate_archive(list_clean: list, name: str):
    """From the plugin folder, generate an archive to test his code"""
    archive_path_source = pathlib.Path(os.getcwd(), name)
    archive_filename = pathlib.Path(os.getcwd(), f"{name}.zip")
    archive_file_generate = zipfile.ZipFile(archive_filename, 'w')

    try:
        # Check if all default folder are present.
        if not archive_path_source.exists():
            raise ArchiveFolderSourceNotFound(source=name)

        for directory, subdir, files in os.walk(archive_path_source):
            if '__pycache__' not in directory:
                for file in files:
                    append_file = pathlib.Path(directory, file)
                    included_file = pathlib.Path(os.path.relpath(append_file))
                    archive_file_generate.write(append_file, included_file)

        archive_file_generate.close()
        list_clean.append(archive_filename)

    except BaseException as e:
        print(f'Generate Archive error : \n\t{e}')
        sys.exit(1)


def ordering_test_file():
    unit_test_folder = pathlib.Path(os.getcwd(), "tests", "unit_test")
    unit_test = os.listdir(unit_test_folder)
    unit_test_b3d = []
    unit_test_ue = []

    for test in unit_test:
        if '_ue_' in test:
            unit_test_ue.append(test)
        elif '_b3d_' in test:
            unit_test_b3d.append(test)

    return {'blender': unit_test_b3d, 'unreal': unit_test_ue}
