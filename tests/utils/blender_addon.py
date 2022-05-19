import os
import bpy
import pathlib
import json
import shutil


def b3d_install_addon():
    """Function to install addon with the blender locally set"""
    env_name = 'FOLDER_TEST'
    dependency = pathlib.Path(os.environ[env_name], "tests", "dependency.json")
    with open(dependency) as f:
        data = json.load(f)

    b3d_dependency = data['blender']

    try:
        if not os.environ.get(env_name):
            raise KeyError
        env_path = pathlib.Path(os.environ[env_name])
        if not env_path.exists():
            raise FileNotFoundError

        for key, value in b3d_dependency.items():
            bpy.ops.preferences.addon_install(filepath=f'{env_path}/{value[0]}')
            bpy.ops.preferences.addon_enable(module=key)
            bpy.ops.wm.save_userpref()

    except KeyError:
        print(f'Env. "{env_name}" doesn\'t exist')
        exit(1)
    except FileNotFoundError:
        print('Wrong path to execute this Unit Test')
        exit(1)


def b3d_install_preset():
    """If the folder preset exist, add all preset inside the moderlab dedicated folder"""
    env_name = 'FOLDER_TEST'

    try:
        if not os.environ.get(env_name):
            raise KeyError

        path_preset = pathlib.Path(bpy.utils.preset_paths("")[0])
        path_locally = pathlib.Path(os.environ.get(env_name), "presets")

        if path_locally.exists():
            shutil.copytree(path_locally, path_preset.joinpath("moderlab", "props"))

    except KeyError:
        print(f'Env. "{env_name}" doesn\'t exist')
        exit(1)


if __name__ == '__main__':
    b3d_install_addon()
    b3d_install_preset()
