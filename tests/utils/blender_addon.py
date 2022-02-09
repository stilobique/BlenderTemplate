import sys
import bpy

# Paste this variable in the blender.py
dependency = {
    # 'moderlab_plugin': ['moderlab_plugin.zip', 'Moderlab-Production/BlenderPlugin'],
    'moderlab_type': ['moderlab_type.zip', 'Moderlab-Production/BlenderObjectType'],
    # 'moderlab_pie': ['moderlab_pie.zip', 'Moderlab-Production/BlenderPieMenu'],
    # 'uv-packer': ['uv-packer.zip', 'Moderlab-Production/UvPacker'],
}


def b3d_install_addon():
    for key, value in dependency.items():
        bpy.ops.preferences.addon_install(filepath=f'/addon_moderlab/{value[0]}')
        bpy.ops.preferences.addon_enable(module=key)
        bpy.ops.wm.save_userpref()


if __name__ == '__main__':
    b3d_install_addon()
