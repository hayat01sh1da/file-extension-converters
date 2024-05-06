import sys
sys.path.append('./src')
from application import Application

try:
    _, original_extension, target_extension, mode, *_ = sys.argv
except ValueError:
    _, original_extension, target_extension, *_ = sys.argv
    mode                                        = '-d'

Application(original_extension, target_extension, mode).run()
