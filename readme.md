# Blender Addon
Template repository about blender addon. To used-it, clone this repository and rename the folder "blender_addon_folder" with your addon name.
Update the file "tests/main.py", line 29, set your addon name.

````python
    # Prepare Blender and Unreal dependency
    generate_archive(archives, 'blender_addon_folder')
````

> ⚠️ It's more easy to use the "_" with your addon folder name, the "-" character can be problematic with python used. 


# Setup Variable
The Github Workflow (CI chain) request some update with each new repository :
- [ ] Env. variable : request the package ex name. Get a better solution to automatically used the folder name ?


# Unit Test
All unit test call the blender docker [stilobique/blender:latest](https://hub.docker.com/repository/docker/stilobique/blender).