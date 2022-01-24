#!/bin/sh

# To disable the sdt with each command, add ' > /dev/null 2>&1' to redirect all info
# Set all variables
MOUNT_FOLDER="/addon-moderlab"
INSTALL_ADDON="$MOUNT_FOLDER/tests/utils/blender_addon.py"

export FOLDER_TEST=$MOUNT_FOLDER

# ----- ----- ----- -----
# From a previous archive generated, install the moderlab plugin
/opt/blender/blender --background --python "$INSTALL_ADDON" -- "$MOUNT_FOLDER" > /dev/null 2>&1
install_error=$?

if [ $install_error = 1 ]; then
  echo Blender Test Error
  echo Exit code is install_error
  (exit 1)
else
  # ----- ----- ----- -----
  # Launch Blender Test
  /opt/blender/blender --background -noaudio --disable-autoexec --addons moderlab_type --python-exit-code 1 --python "$1" -- --verbose
  blender_error=$?

  if [ $blender_error = 1 ]; then
    echo Blender Test Error
    echo Exit code is $blender_error
    (exit 1)
  fi

fi
