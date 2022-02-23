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

#### Blender addon dependency
With all unit test, if your addon request some dependency, add the repo inside the list in `blender_addon.py` and `blender.py`. This system are not perfect and need to be improved.