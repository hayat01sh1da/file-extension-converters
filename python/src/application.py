import glob
import inspect
import os
import shutil


class Application:
    """Renames files in the current directory tree from one extension to
    another, with a dry-run mode that prints intended renames without
    touching the disk."""

    class InvalidExtensionError(Exception):
        pass

    class InvalidModeError(Exception):
        pass

    @classmethod
    def run(cls, original_extension: str = '', target_extension: str = '',
            mode: str = 'd') -> None:
        instance = cls(
            original_extension=original_extension,
            target_extension=target_extension,
            mode=mode,
        )
        instance.validate_extension()
        instance.validate_mode()
        instance._run()

    def __init__(self, original_extension: str = '',
                 target_extension: str = '', mode: str = 'd') -> None:
        self._original_extension = original_extension
        self._target_extension = target_extension
        self._mode = mode
        self._target_files = glob.glob(
            os.path.join('.', '**', f'*{original_extension}'), recursive=True)

    def validate_extension(self) -> None:
        if (not self._original_extension.startswith('.')
                or not self._target_extension.startswith('.')):
            raise self.InvalidExtensionError(
                'Provide a valid extension starting with `.`')

    def validate_mode(self) -> None:
        match self._mode:
            case 'd' | 'e':
                return
            case _:
                raise self.InvalidModeError(
                    f'{self._mode} is invalid mode. '
                    'Provide either `d`(default) or `e`.'
                )

    # private

    def _run(self) -> None:
        self._output(f'Current Directory is {os.path.abspath(".")}')
        if not self._target_files:
            self._announce_empty()
            return
        self._announce_start()
        self._convert_files()
        self._announce_finish()

    def _announce_empty(self) -> None:
        self._output(
            f'========== [{self._exec_mode()}] '
            f'No File with {self._original_extension} Remains =========='
        )

    def _announce_start(self) -> None:
        self._output(
            f'========== [{self._exec_mode()}] '
            f'Total File Extensions Count to Convert: '
            f'{len(self._target_files)} =========='
        )
        self._output(
            f'========== [{self._exec_mode()}] '
            f'Start Converting File Extensions =========='
        )

    def _convert_files(self) -> None:
        for target_file in self._target_files:
            destination = self._destination_file(target_file)
            if self._mode == 'e':
                shutil.move(target_file, destination)
            self._output(
                f'========== [{self._exec_mode()}] '
                f'Converted File Extension: {target_file} => '
                f'{destination} =========='
            )

    def _announce_finish(self) -> None:
        self._output(
            f'========== [{self._exec_mode()}] '
            f'Total Converted File Extensions Count: '
            f'{len(self._target_files)} =========='
        )

    def _exec_mode(self) -> str:
        return 'EXECUTION' if self._mode == 'e' else 'DRY RUN'

    def _destination_file(self, target_file: str) -> str:
        return (
            f'{os.path.dirname(target_file)}/'
            f'{os.path.splitext(os.path.basename(target_file))[0]}'
            f'{self._target_extension}'
        )

    def _test_env(self) -> bool:
        stack = inspect.stack()
        if not stack:
            return False
        return 'pytest' in os.path.basename(stack[-1].filename)

    def _output(self, message: str) -> None:
        if not self._test_env():
            print(message)
