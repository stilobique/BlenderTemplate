import glob
import os


def get_folder_name():
    addon = glob.glob(os.getcwd() + "/*/__init__.py", recursive=True)

    return os.path.basename(os.path.dirname(addon[0]))


if __name__ == "__main__":
    name = get_folder_name()

    with open('$GITHUB_ENV', 'a') as f:
        f.write(f'APP_NAME={name}')
        f.write(f'NAME_PACKAGE={name}.zip')
