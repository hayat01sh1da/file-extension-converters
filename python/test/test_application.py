import glob
import os

import pytest

from application import Application


ORIGINAL_EXTENSION = '.png'
TARGET_EXTENSION = '.jpg'


def _count(tmp_dir: str, extension: str) -> int:
    return len(glob.glob(
        os.path.join(tmp_dir, '**', f'*{extension}'), recursive=True))


def test_invalid_extension() -> None:
    with pytest.raises(Application.InvalidExtensionError) as excinfo:
        Application.run(
            original_extension='py', target_extension=TARGET_EXTENSION)
    assert str(excinfo.value) == 'Provide a valid extension starting with `.`'


def test_invalid_mode() -> None:
    with pytest.raises(Application.InvalidModeError) as excinfo:
        Application.run(
            original_extension=ORIGINAL_EXTENSION,
            target_extension=TARGET_EXTENSION,
            mode='a',
        )
    assert str(excinfo.value) == (
        'a is invalid mode. Provide either `d`(default) or `e`.'
    )


def test_run_in_dry_run_mode_with_default_mode(tmp_dir: str) -> None:
    Application.run(
        original_extension=ORIGINAL_EXTENSION,
        target_extension=TARGET_EXTENSION,
    )
    assert _count(tmp_dir, ORIGINAL_EXTENSION) == 100
    assert _count(tmp_dir, TARGET_EXTENSION) == 0


def test_run_in_dry_run_mode_with_explicit_d_mode(tmp_dir: str) -> None:
    Application.run(
        original_extension=ORIGINAL_EXTENSION,
        target_extension=TARGET_EXTENSION,
        mode='d',
    )
    assert _count(tmp_dir, ORIGINAL_EXTENSION) == 100
    assert _count(tmp_dir, TARGET_EXTENSION) == 0


def test_run_in_exec_mode(tmp_dir: str) -> None:
    Application.run(
        original_extension=ORIGINAL_EXTENSION,
        target_extension=TARGET_EXTENSION,
        mode='e',
    )
    assert _count(tmp_dir, ORIGINAL_EXTENSION) == 0
    assert _count(tmp_dir, TARGET_EXTENSION) == 100
