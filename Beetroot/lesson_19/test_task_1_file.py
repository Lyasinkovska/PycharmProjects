"""
Writing tests for context manager

Take your implementation of the context manager class from Task 1 and write tests for it. Try to cover as many use
cases as you can, positive ones when a file exists and everything works as designed. And also, write tests when your
class raises errors or you have errors in the runtime context suite.
"""

import unittest

from lesson_19.task_1_file import File


class TestFile(unittest.TestCase):
    def setUp(self) -> None:
        self.readfile = 'test_read_file.txt'
        self.writefile = 'test_write_file.txt'
        self.text = 'This is test file'
        self.write_mode = 'w'
        self.read_mode = 'r'
        self.false_mode = 'l'
        self.__allowed_modes = ('r', 'r+', 'rb', 'w', 'w+', 'wb', 'wb+', 'a', 'a+', 'ab', 'ab+')
        File.counter = 0

    def test_right_mode(self):
        self.mode = self.write_mode if self.write_mode in self.__allowed_modes else 'r'
        self.assertEqual(self.mode, self.write_mode)

    def test_false_mode(self):
        self.mode = self.false_mode if self.false_mode in self.__allowed_modes else 'r'
        self.assertEqual(self.mode, 'r', 'Wrong mode assigned')
        self.assertNotEqual(self.false_mode, self.mode, 'Falsy mode should not equal mode.')

    def test_read_file(self):
        with open(self.readfile, self.read_mode) as file:
            read_file = file.read()
        self.assertIn(self.text, read_file)

    def test_write_to_file(self):
        with open(self.writefile, self.write_mode) as file:
            file.truncate()
            file.write(self.text)

        with open(self.writefile, self.read_mode) as file:
            read_file = file.read()
        self.assertEqual(self.text, read_file, 'text is not in file')

    def test_closed_file(self):
        file = open(self.readfile, self.read_mode)
        self.assertFalse(file.closed, 'file is open')
        file.close()
        self.assertTrue(file.closed, 'file is not closed')

    def test_counter(self):
        new_file = File('new_file.txt', self.write_mode)
        self.assertEqual(new_file.counter, 1, 'only one created instance')


if __name__ == '__main__':
    unittest.main()
