import unittest
import bpy
import glob
import os


class ActivateAddon(unittest.TestCase):
    """Activate the Blender addon"""

    @staticmethod
    def get_folder_name():
        """Return the folder name to get the addon name we want activated"""
        addon = glob.glob("/addon_moderlab/*/__init__.py", recursive=True)
        return os.path.basename(os.path.dirname(addon[0]))

    def test_activate_addon(self):
        """Activate the blender addon 'moderlab_plugin'"""
        addon = bpy.ops.preferences.addon_enable(module=self.get_folder_name())
        self.assertEqual({'FINISHED'}, addon)


if __name__ == '__main__':
    import sys
    sys.argv = [__file__] + (sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else [])
    unittest.main()
