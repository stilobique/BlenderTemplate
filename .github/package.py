import glob
import os


def get_folder_name():
    addon = glob.glob(os.getcwd() + "/*/__init__.py", recursive=True)

    return os.path.basename(os.path.dirname(addon[0]))


if __name__ == "__main__":
    name = get_folder_name()

    # Keep the print value, it's request to output a string value available
    print(name)
