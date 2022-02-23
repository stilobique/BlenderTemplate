import os

from pathlib import PurePosixPath


class ContainerObject(object):
    """All data request to launch one dedicated container"""

    def __init__(self, name: str, image: str):
        self.label: str = name.lower()
        self.image: str = image
        self.tag: str = self.set_tag()
        self.local_folder: str = ''
        self.volumes: list[str] = self.set_volumes()
        self.environments: list[str] = self.set_environments()
        self.commands: list[str] = self.set_commands()
        self.ref = f'{self.image}:{self.tag}'

    def set_tag(self):
        """Determine the tag use with the docker image call"""
        if 'blender' in self.label:
            return 'latest'
        elif 'unreal' in self.label:
            return 'dev-slim-4.27.2'
        else:
            return None

    def set_volumes(self):
        """Define folder/path with mount with each docker container"""
        if 'blender' in self.label:
            self.local_folder = '/addon_moderlab'
        elif 'unreal' in self.label:
            self.local_folder = '/project'
        else:
            return None
        return [f'{self.workspace()}:{self.local_folder}']

    def set_environments(self):
        """Add environment variable start with the docker container"""
        if 'blender' in self.label:
            return [f'FOLDER_TEST={self.local_folder}']
        else:
            return []

    def set_commands(self):
        """Write all commands execute on the docker container start"""
        cmds = ['/bin/sh']
        if 'blender' in self.label:
            cmds.append(str(PurePosixPath(self.local_folder, "tests", "launch_test_b3d.sh")))
        else:
            cmds.append(str(PurePosixPath(self.local_folder, "tests", "launch_test_ue.sh")))
            cmds.append(str(PurePosixPath(self.local_folder, "tests", "unreal_sample", "empty_project",
                                          "EmptyProject.uproject")))

        return cmds

    @staticmethod
    def workspace():
        """Define the workspace folder"""
        if os.environ.get('GITHUB_WORKSPACE'):
            return os.environ['GITHUB_WORKSPACE']
        else:
            return os.getcwd()
