import sys
import os
import enum

from pathlib import Path
from utils.blender import get_b3d_addon_dependency
from utils.container import VirtualMachine
from utils.misc import ordering_test_file, generate_archive
from utils.properties import ContainerObject


class Container(enum.Enum):
    """Enumerate about the Geometry node"""
    BLENDER = ContainerObject(name='Blender', image='stilobique/blender')


def launch_unit_test(test: [str] = None):
    """Start all Unit Test, Blender and Unreal if needed"""
    # Ordering Unit test Blender/Unreal
    if test is None:
        test = ordering_test_file()
        b3d = test['blender']
    else:
        b3d = test

    vm_b3d = VirtualMachine(Container.BLENDER.value)
    vm_b3d.launch_unit_test(tests=b3d)


if __name__ == '__main__':
    # Initialize Variable and module request
    archives = []

    # Prepare Blender and Unreal dependency
    get_b3d_addon_dependency(archives)
    generate_archive(archives, 'blender_addon_folder')

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
    launch_unit_test(test=test_list)

    # Clear archive file and container
    for archive in archives:
        if Path(Path(os.getcwd(), archive)).exists():
            os.remove(Path(os.getcwd(), archive))
