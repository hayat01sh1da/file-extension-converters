import glob
import os

import pytest

from application import Application, InvalidExtensionError, InvalidModeError


ORIGINAL_EXTENSION = '.txt'
TARGET_EXTENSION = '.md'


def _count(tmp_dir: str, extension: str) -> int:
    return len(
        glob.glob(
            os.path.join(
                tmp_dir,
                '**',
                f'*{extension}'),
            recursive=True))


def test_invalid_extension(tmp_dir: str) -> None:
    with pytest.raises(InvalidExtensionError) as excinfo:
        Application(original_extension='py',
                    target_extension=TARGET_EXTENSION).run()
    assert str(excinfo.value) == 'Provide a valid extension starting with `.`'


def test_invalid_mode(tmp_dir: str) -> None:
    with pytest.raises(InvalidModeError) as excinfo:
        Application(
            original_extension=ORIGINAL_EXTENSION,
            target_extension=TARGET_EXTENSION,
            mode='a',
        ).run()
    assert str(
        excinfo.value) == 'a is invalid mode. Provide either `d`(default) or `e`.'


@pytest.mark.parametrize('mode', [None, 'd'])
def test_run_in_dry_run_mode(tmp_dir: str, mode: str | None) -> None:
    kwargs = {
        'original_extension': ORIGINAL_EXTENSION,
        'target_extension': TARGET_EXTENSION}
    if mode is not None:
        kwargs['mode'] = mode
    Application(**kwargs).run()
    assert _count(tmp_dir, ORIGINAL_EXTENSION) == 100
    assert _count(tmp_dir, TARGET_EXTENSION) == 0


def test_run_in_exec_mode(tmp_dir: str) -> None:
    Application(
        original_extension=ORIGINAL_EXTENSION,
        target_extension=TARGET_EXTENSION,
        mode='e',
    ).run()
    assert _count(tmp_dir, ORIGINAL_EXTENSION) == 0
    assert _count(tmp_dir, TARGET_EXTENSION) == 100
