import unittest
import os
import glob
import shutil
import sys
sys.path.append('./src')
from application import Application

class TestApplication(unittest.TestCase):
    def setUp(self):
        self.dirname = os.path.join('.', 'test', 'tmp')
        if not os.path.isdir(self.dirname):
            os.makedirs(self.dirname)
        self.original_extension = '.txt'
        for i in range(1, 101):
            with open(os.path.join(self.dirname, 'test_file_{i:03}{original_extension}'.format(i = i, original_extension = self.original_extension)), 'w') as f:
                f.write('')
        self.target_extension = '.md'

    def test_run_in_dry_run_mode_1(self):
      Application(self.original_extension, self.target_extension).run()
      self.assertEqual(len(glob.glob(os.path.join(self.dirname, '**', '*{original_extension}'.format(original_extension = self.original_extension)), recursive = True)), 100)
      self.assertEqual(len(glob.glob(os.path.join(self.dirname, '**', '*{target_extension}'.format(target_extension = self.target_extension)), recursive = True)), 0)

    def test_run_in_dry_run_mode_2(self):
      Application(self.original_extension, self.target_extension, '-d').run()
      self.assertEqual(len(glob.glob(os.path.join(self.dirname, '**', '*{original_extension}'.format(original_extension = self.original_extension)), recursive = True)), 100)
      self.assertEqual(len(glob.glob(os.path.join(self.dirname, '**', '*{target_extension}'.format(target_extension = self.target_extension)), recursive = True)), 0)

    def test_run_in_exec_mode(self):
      Application(self.original_extension, self.target_extension, '-e').run()
      self.assertEqual(len(glob.glob(os.path.join(self.dirname, '**', '*{original_extension}'.format(original_extension = self.original_extension)), recursive = True)), 0)
      self.assertEqual(len(glob.glob(os.path.join(self.dirname, '**', '*{target_extension}'.format(target_extension = self.target_extension)), recursive = True)), 100)

    def tearDown(self):
        shutil.rmtree(self.dirname)

if __name__ == '__main__':
    unittest.main()
