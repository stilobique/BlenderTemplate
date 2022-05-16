[![Python 3.10.2](https://img.shields.io/badge/python-3.10.2-sucess.svg)](https://www.python.org/downloads/release/python-3102/)
![Blender](https://img.shields.io/badge/blender-3.1.0-sucess)

# Blender Addon
This repository is a toolbox to create a new blender addon. To used-it, clone this repository and rename the folder "blender_addon_folder" with your addon name.
It's important to change some files :
- [x] Update the file "tests/main.py", line 29, set your addon name.
  ```python
  # Prepare Blender and Unreal dependency
  generate_archive(archives, 'blender_addon_folder')
  ```
- [x] You can remove the folder "presets" and disable the workflow (`.github/workflows/pr_main.yml`, line 38 and 53)


> ⚠️ It's more easy to use the "_" with your addon folder name, the "-" character can be problematic with python use. 

All features covered with this template are :
- [x] Generate addon release (.zip archive)
- [x] Generate preset release (.zip archive)
- [x] Update addon version (bl info) with tag name
- [x] Execute unit test with Github Action (check if the addon can be installed with blender)
- [x] Configuration with Pycharm to test locally


## Unit Test
All unit tests call docker image [stilobique/blender](https://hub.docker.com/repository/docker/stilobique/blender). It's a simple ubuntu image with blender compile. 
If you want change the blender version tested, edit the `main.py` inside the `tests` folder ; change the tag version with your requested tag.

`````python
class Container(enum.Enum):
    """Enumerate about the Geometry node"""
    BLENDER = ContainerObject(name='Blender', image='stilobique/blender', tag='3.1.2')
`````


# Addons/Plugins dependency
Update json file `tests/dependency.json` with name, archive and repository Github path. Each entry require `archive 
name`, the repository url path '{owner}/{repo}' and optional parameter if the release needed to be a prerelease.

> ⛔ The `moderlab_plugin` need to be on last entry.
