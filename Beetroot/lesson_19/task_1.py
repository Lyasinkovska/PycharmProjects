"""
File Context Manager class
Create your own class, which can behave like a built-in function `open`. Also, you need to extend its functionality
with counter and logging. Pay special attention to the implementation of `__exit__` method, which has to cover all
the requirements to context managers mentioned here:
"""
import logging

logging.basicConfig(filename='files_opened.log', level=logging.INFO, filemode='a',
                    format=f'%(name)s - %(levelname)s - %(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')


class File:
    counter = 0

    def __init__(self, filename, mode):
        self.mode = mode
        self.filename = filename
        self.file = open(self.filename, self.mode)
        logging.info(f'file: {self.filename}')
        File.counter += 1

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


if __name__ == '__main__':

    with File('sample.txt', 'w') as f:
        for i in range(10):
            f.write(f'Hello {i}\n')

    with File('new_file.txt', 'w') as h:
        for i in range(10):
            h.write(f'Hello {i}\n')
    print(File.counter)
