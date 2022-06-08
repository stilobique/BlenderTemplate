import sys
import os
import pathlib

from pylint import lint


if __name__ == "__main__":
    folder: str = ''
    for v in sys.argv:
        if '--module=' in v:
            folder = v.replace('--module=', '')

    if folder is False:
        print(f'Module folder not set.')
        sys.exit(1)

    run = lint.Run([f'--rcfile={pathlib.Path(os.getcwd(), "linter", ".pylintrc")}', folder],
                   do_exit=False)

    if run.linter.stats.fatal or run.linter.stats.error:
        print('Pylint failed.')
        sys.exit(1)

    sys.exit(0)
