import sys
import os
import shutil
import glob
sys.path.append('./src')
from application import Application

original_extension = input('Provide the original extension of the files you would like to change(e.g., .jpg, .png, .rb, .py, .ts. .js etc.): ')
target_extension   = input('Provide the target extension of the files you would like to switch to by the change(e.g., .jpg, .png, .rb, .py, .ts. .js etc.): ')
mode               = input('Provide d(dry_run: default) to make sure what directories and files are to be changed in the extensions first. Then, provide e(execution) if you would truly like to change the extensions. This operation is cannot be undone, so be alert to your operation!: ')

Application(
    original_extension = original_extension,
    target_extension = target_extension,
    mode = mode,
).run()

pycaches = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)
for pycache in pycaches:
    if os.path.exists(pycache):
        shutil.rmtree(pycache)
