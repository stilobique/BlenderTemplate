import os
import docker
import sys

from pathlib import PurePosixPath, Path


class ErrorTest(Exception):
    """ Failed to generate the test """


def b3d_launch_blender_test(client: docker = docker.from_env(), test: list = None,
                            tag: str = 'stilobique/blender:latest'):
    """Launch blender and a list of Test, you can set a specific test file with his arg."""
    unit_test_folder = Path(os.getcwd(), "tests", "unit_test")

    if os.environ.get('GITHUB_WORKSPACE'):
        local_path = os.environ.get('GITHUB_WORKSPACE')
    else:
        local_path = os.getcwd()
    container_folder = '/addon_moderlab'
    volume = [f'{local_path}:{container_folder}']
    image_name = tag
    if test is None:
        unit_test = os.listdir(unit_test_folder)
    else:
        if type(test) is not list:
            test = [test]
        unit_test = test

    try:
        for test in unit_test:
            print(f'Start this test : {test}')
            command = [f"/bin/sh",
                       f"{PurePosixPath(container_folder, 'tests', 'launch_test.sh')}",
                       f"{PurePosixPath(container_folder, 'tests', 'unit_test', test)}"]

            docker_test = client.containers.run(image_name, command=command, volumes=volume, privileged=True,
                                                environment=[f'FOLDER_TEST={container_folder}'], detach=True, name=test)
            exit_docker = docker_test.wait()
            if exit_docker['StatusCode'] != 0:
                print(f'Container error "{exit_docker["StatusCode"]}".\n\t'
                      f'Show log : \n\t'
                      f'{docker_test.logs()}')
                raise ErrorTest

    except ErrorTest as exception:
        print(f'{exception.__doc__}')
        sys.exit(1)
