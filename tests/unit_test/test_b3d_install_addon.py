import unittest
import bpy


class ActivateAddon(unittest.TestCase):
    """Activate the Blender addon"""

    def setUp(self) -> None:
        pass

    def test_activate_addon(self):
        """Activate the blender addon 'moderlab_plugin'"""
        addon = bpy.ops.preferences.addon_enable(module='moderlab_type')
        self.assertEqual({'FINISHED'}, addon)


if __name__ == '__main__':
    import sys
    sys.argv = [__file__] + (sys.argv[sys.argv.index("--") + 1:] if "--" in sys.argv else [])
    unittest.main()
