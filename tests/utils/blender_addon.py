import bpy
import os
import pathlib

# Paste this variable in the blender.py
dependency = {
    # 'moderlab_plugin': ['moderlab_plugin.zip', 'Moderlab-Production/BlenderPlugin'],
    # 'moderlab_type': ['moderlab_type.zip', 'Moderlab-Production/BlenderObjectType'],
    # 'moderlab_pie': ['moderlab_pie.zip', 'Moderlab-Production/BlenderPieMenu'],
    # 'uv-packer': ['uv-packer.zip', 'Moderlab-Production/UvPacker'],
}


def b3d_install_addon():
    env_name = 'FOLDER_TEST'
    try:
        if not os.environ.get(env_name):
            raise KeyError
        env_path = pathlib.Path(os.environ[env_name])
        if not env_path.exists():
            raise FileNotFoundError

        for key, value in dependency.items():
            bpy.ops.preferences.addon_install(filepath=f'{env_path}/{value[0]}')
            bpy.ops.preferences.addon_enable(module=key)
            bpy.ops.wm.save_userpref()

    except KeyError:
        print(f'Env. "{env_name}" doesn\'t exist')
        exit(1)
    except FileNotFoundError:
        print('Wrong path to execute this Unit Test')
        exit(1)


if __name__ == '__main__':
    b3d_install_addon()
