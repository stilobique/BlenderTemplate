import sys
import os

from pathlib import Path
from utils.blender import b3d_launch_blender_test
from utils.container import clear_container_test
from utils.misc import ordering_test_file, generate_archive


def launch_unit_test(tag: str, test: list = None):
    """Start all Unit Test, Blender and Unreal if needed"""
    test = ordering_test_file()
    b3d_launch_blender_test(test=test['blender'], tag=tag)


if __name__ == '__main__':
    # Initialize Variable and module request
    archives = []
    docker_tag = 'stilobique/blender:latest'

    # Clear blender container
    clear_container_test(tag=docker_tag)

    # Prepare Blender and Unreal dependency
    generate_archive(archives, 'blender-folder')

    # Generate Unit Test, a specific call or execute all Unit Test
    test_list = None
    if sys.argv:
        for arg in sys.argv:
            if '--test=' in arg:
                test_list = []
                items = arg.replace('--test=', '').split(',')
                for item in items:
                    print('Launch this test : ', item)
                    test_list.append(item)

    # Launch Unit Test
    launch_unit_test(test=test_list, tag=docker_tag)

    # Clear archive file and container
    clear_container_test(tag=docker_tag)
    for archive in archives:
        os.remove(Path(os.getcwd(), archive))
