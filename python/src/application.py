import os
import glob
import shutil
import inspect

class InvalidModeError(Exception):
    pass

class Application:
    def __init__(self, original_extension, target_extension, mode = 'd'):
        self.target_files     = glob.glob(os.path.join('.', '**', '*{original_extension}'.format(original_extension = original_extension)), recursive = True)
        self.target_extension = target_extension
        self.mode             = mode
        self.env              = inspect.stack()[1].filename.split('/')[-2]

    def run(self):
        self.__validate__(self.mode)

        self.__output__('Target dirname is {current_directory}'.format(current_directory = os.path.abspath('.')))
        if len(self.target_files) > 1:
            self.__output__('========== [{exec_mode}] Total File Extensions Count to Convert: {files_count} =========='.format(exec_mode = self.__exec_mode__(), files_count = len(self.target_files)))
            self.__output__('========== [{exec_mode}] Start Converting File Extensions'.format(exec_mode = self.__exec_mode__()))
            for target_file in self.target_files:
                self.__output__('========== [{exec_mode}] Cleaning {target_file} =========='.format(exec_mode = self.__exec_mode__(), target_file = target_file))
                if self.mode == 'e':
                    shutil.move(target_file, self.__destination_file__(target_file))
                self.__output__('========== [{exec_mode}] Converted File Extension: {target_file} => {destination_file} =========='.format(exec_mode = self.__exec_mode__(), target_file = target_file, destination_file = self.__destination_file__(target_file)))
            self.__output__('========== [{exec_mode}] Total Converted File Extensions Count: {files_count} =========='.format(exec_mode = self.__exec_mode__(), files_count = len(self.target_files)))
        else:
            self.__output__('========== [{exec_mode}] No File with {original_extension} Remains =========='.format(exec_mode = self.__exec_mode__(), original_extension = self.original_extension))

    # private

    def __validate__(self, mode):
        match mode:
            case 'd' | 'e':
                return
            case _:
                raise InvalidModeError('{mode} is invalid mode. Provide either `d`(default) or `e`.'.format(mode = self.mode))

    def __exec_mode__(self):
        if self.mode == 'e':
            return 'EXECUTION'
        else:
            return 'DRY_RUN'

    def __destination_file__(self, target_file):
        return '{dirname}/{basename}{target_extension}'.format(dirname = os.path.dirname(target_file), basename = os.path.splitext(os.path.basename(target_file))[0], target_extension = self.target_extension)

    def __is_test_env__(self):
        return self.env == 'test'

    def __output__(self, message):
        if not self.__is_test_env__():
            print(message)
