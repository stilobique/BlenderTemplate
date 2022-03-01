# Blender Addon
Template repository about blender addon. To used-it, clone this repository and rename the folder "blender_addon_folder" with your addon name.
Update the file "tests/main.py", line 29, set your addon name.

```python
    # Prepare Blender and Unreal dependency
    generate_archive(archives, 'blender_addon_folder')
```

> ⚠️ It's more easy to use the "_" with your addon folder name, the "-" character can be problematic with python use. 


# Unit Test
All unit tests call docker image [stilobique/blender:latest](https://hub.docker.com/repository/docker/stilobique/blender).

# Addons/Plugins dependency
Update json file `tests/dependency.json` with name, archive and repository Github path. Each entry requiert `archive 
name`, the repository url path '{owner}/{repo}' and optional parameter if the release needed to be a prerelease.

> ⛔ The `moderlab_plugin` need to be on last entry.
