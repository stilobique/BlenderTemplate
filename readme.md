[![Python 3.10.2](https://img.shields.io/badge/python-3.10.2-sucess.svg)](https://www.python.org/downloads/release/python-3102/)
![Blender](https://img.shields.io/badge/blender-3.1.0-sucess)

# Blender Addon
Template repository about blender addon. To used-it, clone this repository and rename the folder "blender_addon_folder" with your addon name.
It's important to change some files :
- [x] Update the file "tests/main.py", line 29, set your addon name.
  ```python
  # Prepare Blender and Unreal dependency
  generate_archive(archives, 'blender_addon_folder')
  ```
- [x] You can remove the folder "presets" and disable the workflow (`.github/workflows/pr_main.yml`, line 38 and 53)


> ⚠️ It's more easy to use the "_" with your addon folder name, the "-" character can be problematic with python use. 


# Unit Test
All unit tests call docker image [stilobique/blender:latest](https://hub.docker.com/repository/docker/stilobique/blender).

# Addons/Plugins dependency
Update json file `tests/dependency.json` with name, archive and repository Github path. Each entry requiert `archive 
name`, the repository url path '{owner}/{repo}' and optional parameter if the release needed to be a prerelease.

> ⛔ The `moderlab_plugin` need to be on last entry.
