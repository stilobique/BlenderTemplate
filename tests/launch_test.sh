#!/bin/bash
/opt/blender/blender --background --python-exit-code 1 --python "$FOLDER_TEST/tests/utils/blender_addon.py" || exit 1 > /dev/null 2>&1
/opt/blender/blender --background -noaudio --disable-autoexec --python-exit-code 1 --python "$1" -- --verbose || exit 1