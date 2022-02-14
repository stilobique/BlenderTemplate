#!/bin/bash
MOUNT_FOLDER="addon_moderlab"
export FOLDER_TEST=$MOUNT_FOLDER
/opt/blender/blender --background --python-exit-code 1 --python "/addon_moderlab/tests/utils/blender_addon.py" > /dev/null 2>&1 || exit 1
/opt/blender/blender --background -noaudio --disable-autoexec --python-exit-code 1 --python "$1" -- --verbose || exit 1