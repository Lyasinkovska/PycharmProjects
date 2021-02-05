"""
File Context Manager class
Create your own class, which can behave like a built-in function `open`. Also, you need to extend its functionality
with counter and logging. Pay special attention to the implementation of `__exit__` method, which has to cover all
the requirements to context managers mentioned here:
"""
import logging


class File:
    counter = 0

    def __init__(self, filename, mode):
        self.__allowed_modes = ('r', 'r+', 'rb', 'w', 'w+', 'wb', 'wb+', 'a', 'a+', 'ab', 'ab+')
        self.mode = mode if mode in self.__allowed_modes else 'r'
        self.filename = filename
        logging.basicConfig(filename='files_opened.log', level=logging.INFO, filemode='a',
                            format=f'%(name)s - %(levelname)s - %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
        File.counter += 1

    def __enter__(self):
        try:
            self.file = open(self.filename, self.mode)
            return self.file
        except IOError:
            logging.info(f'file {File.counter}: {self.filename}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            logging.error(f'file {File.counter}: {self.filename}, raised exception:({exc_type.__name__})')
        self.file.close()


if __name__ == '__main__':

    with File('sample.txt', 'l') as f:
        print(f.read())

    with File('next_file.txt', 'w') as h:
        for i in range(5):
            h.write(f'Hello {i}\n')
    print(h.closed)
