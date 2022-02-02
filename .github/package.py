import glob
import os


def get_folder_name():
    addon = glob.glob(os.getcwd() + "/*/__init__.py", recursive=True)

    return os.path.basename(os.path.dirname(addon[0]))


if __name__ == "__main__":
    env_file = os.getenv('GITHUB_ENV')
    name = get_folder_name()
    print(f'Python : The folder name find are "{name}"')

    with open(env_file, 'a') as f:
        f.write(f'APP_NAME={name}')
        f.write(f'NAME_PACKAGE={name}.zip')
        print('Update all env. variable')
        f.close()
