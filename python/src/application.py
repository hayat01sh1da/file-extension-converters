import os
import glob
import shutil
import inspect

class InvalidExtensionError(Exception):
    pass

class InvalidModeError(Exception):
    pass

class Application:
    def __init__(self, original_extension: str, target_extension: str, mode: str = 'd') -> None:
        self.original_extension: str = original_extension
        self.target_files: list[str] = glob.glob(os.path.join('.', '**', f'*{original_extension}'), recursive = True)
        self.target_extension: str   = target_extension
        self.mode: str               = mode
        self.exec_mode: str          = self.__exec_mode__()
        self.env: str                = inspect.stack()[1].filename.split('/')[-2]

    def run(self) -> None:
        self.__validate_extension__()
        self.__validate_mode__()

        self.__output__(f'Target dirname is {os.path.abspath(".")}')
        if len(self.target_files) > 1:
            self.__output__(f'========== [{self.__exec_mode__()}] Total File Extensions Count to Convert: {len(self.target_files)} ==========')
            self.__output__(f'========== [{self.__exec_mode__()}] Start Converting File Extensions')
            for target_file in self.target_files:
                self.__output__(f'========== [{self.__exec_mode__()}] Cleaning {target_file} ==========')
                if self.mode == 'e':
                    shutil.move(target_file, self.__destination_file__(target_file))
                self.__output__(f'========== [{self.__exec_mode__()}] Converted File Extension: {target_file} => {self.__destination_file__(target_file)} ==========')
            self.__output__(f'========== [{self.__exec_mode__()}] Total Converted File Extensions Count: {len(self.target_files)} ==========')
        else:
            self.__output__(f'========== [{self.__exec_mode__()}] No File with {self.original_extension} Remains ==========')

    # private

    def __validate_extension__(self) -> None:
        if not self.original_extension.startswith('.') or not self.target_extension.startswith('.'):
            raise InvalidExtensionError('Provide a valid extension starting with `.`')

    def __validate_mode__(self) -> None:
        match self.mode:
            case 'd' | 'e':
                return
            case _:
                raise InvalidModeError(f'{self.mode} is invalid mode. Provide either `d`(default) or `e`.')

    def __exec_mode__(self) -> str:
        if self.mode == 'e':
            return 'EXECUTION'
        else:
            return 'DRY_RUN'

    def __destination_file__(self, target_file: str) -> str:
        return f'{os.path.dirname(target_file)}/{os.path.splitext(os.path.basename(target_file))[0]}{self.target_extension}'

    def __is_test_env__(self) -> bool:
        return self.env == 'test'

    def __output__(self, message: str) -> None:
        if not self.__is_test_env__():
            print(message)
