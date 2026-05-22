import os
import sys

from invoke import Context, task

_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(_ROOT, 'src'))

from application import Application  # noqa: E402


@task
def run_file_extension_converter(c: Context) -> None:
    """Run File Extension Converter"""
    print('Provide the original extension of the files you would like '
          'to change(e.g., .jpg, .png, .rb, .py, .ts. .js etc.)')
    original_extension = input().strip()

    print('Provide the target extension of the files you would like to '
          'switch to by the change(e.g., .jpg, .png, .rb, .py, .ts. .js '
          'etc.)')
    target_extension = input().strip()

    print('Provide d(dry_run: default) to make sure what directories '
          'and files are to be changed in the extensions first. Then, '
          'provide e(execution) if you would truly like to change the '
          'extensions. This operation is cannot be undone, so be alert '
          'to your operation!')
    mode = input().strip()

    params: dict[str, str] = {}
    for key, value in {
        'original_extension': original_extension,
        'target_extension': target_extension,
        'mode': mode,
    }.items():
        if value:
            params[key] = value

    Application(**params).run()


@task(default=True)
def test(c: Context) -> None:
    """Run all tests"""
    c.run('pytest .')
