import glob
import os


def get_folder_name():
    addon = glob.glob(os.getcwd() + "/*/__init__.py", recursive=True)

    return os.path.basename(os.path.dirname(addon[0]))


if __name__ == "__main__":
    env_file = os.getenv('GITHUB_ENV')
    name = get_folder_name()
    archive = name + '.zip'
    print(f'Python : The folder name find are "{name}"')

    with open(env_file, 'w') as f:
        f.write('APP_NAME={name}'.format(name=name))
        f.write('NAME_PACKAGE={archive}.zip'.format(archive=archive))
        print('Update all env. variable')
