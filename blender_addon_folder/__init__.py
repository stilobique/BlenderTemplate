import bpy

bl_info = {
    'name': 'Addon Name',
    'description': 'Add your description',
    'author': 'Moderlab, Aurelien Vaillant, Nicolas Salles, Jeremy Duchesne',
    'version': (0, 0, 0),
    'blender': (3, 0, 0),
    'doc_url': "",
    'tracker_url': "",
    'support': "COMMUNITY",
    'category': 'Moderlab',
}

modules_class = [
    # Main Property
]


def register():
    for cls in modules_class:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(modules_class):
        bpy.utils.unregister_class(cls)


if __name__ == "__main__":
    register()
