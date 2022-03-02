import docker
import os
import sys

from pathlib import PurePosixPath
from docker.errors import DockerException
from .issue import ContainerErrorTest
from .properties import ContainerObject
from .misc import read_token


class VirtualMachine:
    def __init__(self, container: ContainerObject):
        self.client = self.start_docker()

        self.container = container
        self.base_command = self.container.commands

        self.clear_containers()
        self.pull_image()

    @staticmethod
    def start_docker():
        """Generate docker client information"""
        try:
            client = docker.from_env()
            return client

        except DockerException:
            print('Docker isn\'t start or installed')
            exit(1)

    def pull_image(self):
        """Pull docker image"""
        print(f'Pull this image : {self.container.image}')
        if 'unreal' in self.container.label:
            unreal_token = read_token('token_unreal.txt')
            self.client.login(registry='https://ghcr.io', username='stilobique', password=unreal_token)

        print('Start to PULL image')
        self.client.images.pull(f'{self.container.image}:{self.container.tag}')
        print('Image is pull')

    def clear_containers(self):
        """Look all docker containers, and remove-it if the task are used with the unit test."""
        containers = self.client.containers.list(all=True)

        for container in containers:
            image_tag = container.image.tags[0]
            status = container.status
            if image_tag in self.container.ref and status in 'exited':
                container.remove()

    @staticmethod
    def workspace():
        """Define the workspace folder"""
        if os.environ.get('GITHUB_WORKSPACE'):
            return os.environ['GITHUB_WORKSPACE']
        else:
            return os.getcwd()

    def launch_unit_test(self, tests: list[str]):
        """Execute a docker container to start unit test dedicated"""
        if tests is None:
            unit_test = os.listdir(self.workspace())
        else:
            if type(tests) is not list:
                tests = [tests]
            unit_test = tests

        try:
            for test in unit_test:
                print(f'Launch unit test "{test}"')
                cmds = self.base_command + [f'{PurePosixPath(self.container.local_folder, "tests", "unit_test", test)}']

                docker_test = self.client.containers.run(self.container.ref, command=cmds,
                                                         volumes=self.container.volumes, privileged=True,
                                                         environment=self.container.environments, detach=True,
                                                         name=test, tty=True)
                exit_docker = docker_test.wait()
                if exit_docker['StatusCode'] != 0:
                    print(f'Container error "{exit_docker["StatusCode"]}".\n\t'
                          f'Show log : \n\t'
                          f'{docker_test.logs()}')
                    raise ContainerErrorTest

        except ContainerErrorTest as exception:
            print(f'{exception.__doc__}')
            sys.exit(1)
