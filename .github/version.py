import os
import re
import sys

from pathlib import Path


class SetupVersion:
    def __init__(self, version: str, folder: str):
        self.addon_file = Path(os.getcwd(), folder, '__init__.py')
        self.tag = self.conform_tag_to_blender(version)
        self.update_addon_init()

    def update_addon_init(self):
        """Simple function to update the bl_info to set the Git tag release"""
        regex, update = r'[0-9]{1,2}\, [0-9]{1,2}\, [0-9]{1,2}', ''

        try:
            with open(self.addon_file, "r") as f:
                i = 0
                lines = f.readlines()
                for line in lines:
                    if '    \'version\':' in line:
                        print('Actual set : ', line)
                        line = re.sub(regex, self.tag, line)
                        lines[i] = line
                        update = lines
                        print('Update version : ', line)
                        break
                    i += 1

            with open(self.addon_file, 'w') as f:
                f.writelines(update)

        except FileNotFoundError as exception:
            print(f'Can\'t find a file :\n\t{exception}')

    @staticmethod
    def conform_tag_to_blender(version):
        """This function convert all '.' with a coma and remove the alphabetic entry, to be ready with blender 'bl
        info' value """
        version = re.sub(r'\.', ', ', version)
        version = version.replace('v', '')

        return version


class SetupError(Exception):
    """No tag or folder name valid"""
    pass


if __name__ == "__main__":
    tag, name = '', ''

    for value in sys.argv:
        if '--tag' in value:
            tag = value.replace('--tag=', '')
            print(f'[UpdateVersion] Set the tag {tag}')

        if 'name' in value:
            name = value.replace('--name=', '')
            print(f'[UpdateVersion] Set the folder {name}')

    try:
        if not tag or not name:
            raise SetupError
        else:
            print(f'[UpdateVersion] Set the tag {tag}, for "{name}"')
            bump = SetupVersion(tag, name)

    except SetupError:
        print(SetupError.__doc__)
        sys.exit(1)
