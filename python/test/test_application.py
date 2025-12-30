import unittest
import os
import glob
import shutil
import sys
sys.path.append('./src')
from application import Application, InvalidExtensionError, InvalidModeError

class TestApplication(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.join('.', 'test', 'tmp')
        if not os.path.exists(self.dirname):
            os.makedirs(self.dirname)
        self.original_extension = '.txt'
        for i in range(1, 101):
            with open(os.path.join(self.dirname, f'test_file_{i:03}{self.original_extension}'), 'w') as f:
                f.write('')
        self.target_extension = '.md'
        self.pycaches         = glob.glob(os.path.join('.', '**', '__pycache__'), recursive = True)

    def tearDown(self):
        if os.path.exists(self.dirname):
            shutil.rmtree(self.dirname)
        for pycache in self.pycaches:
            if os.path.exists(pycache):
                shutil.rmtree(pycache)

    def test_invalid_extension(self):
        with self.assertRaises(InvalidExtensionError) as cm:
            Application(original_extension = 'py', target_extension = self.target_extension).run()
        self.assertEqual('Provide a valid extension starting with `.`', str(cm.exception))

    def test_invalid_mode(self):
        with self.assertRaises(InvalidModeError) as cm:
            Application(original_extension = self.original_extension,  target_extension = self.target_extension, mode = 'a').run()
        self.assertEqual('a is invalid mode. Provide either `d`(default) or `e`.', str(cm.exception))

    def test_run_in_dry_run_mode_1(self):
      Application(original_extension = self.original_extension,  target_extension = self.target_extension ).run()
      self.assertEqual(len(glob.glob(os.path.join(self.dirname, '**', f'*{self.original_extension}'), recursive = True)), 100)
      self.assertEqual(len(glob.glob(os.path.join(self.dirname, '**', f'*{self.target_extension}'), recursive = True)), 0)

    def test_run_in_dry_run_mode_2(self):
      Application(original_extension = self.original_extension,  target_extension = self.target_extension, mode = 'd').run()
      self.assertEqual(len(glob.glob(os.path.join(self.dirname, '**', f'*{self.original_extension}'), recursive = True)), 100)
      self.assertEqual(len(glob.glob(os.path.join(self.dirname, '**', f'*{self.target_extension}'), recursive = True)), 0)

    def test_run_in_exec_mode(self):
      Application(original_extension = self.original_extension, target_extension = self.target_extension, mode = 'e').run()
      self.assertEqual(len(glob.glob(os.path.join(self.dirname, '**', f'*{self.original_extension}'), recursive = True)), 0)
      self.assertEqual(len(glob.glob(os.path.join(self.dirname, '**', f'*{self.target_extension}'), recursive = True)), 100)

if __name__ == '__main__':
    unittest.main()
