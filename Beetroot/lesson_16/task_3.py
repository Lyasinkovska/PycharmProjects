"""Create your own implementation of an iterable, which could be used inside for-in loop. Also, add logic for
retrieving elements using square brackets syntax."""
from lesson_16.task_2 import InRange


class IterObj:

    def __init__(self, *args):
        self.__iter_obj = [*args]
        self.__start = 0
        self.__stop = len(self.__iter_obj)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__start >= self.__stop:
            raise StopIteration
        self.__start += 1
        return self.__iter_obj[self.__start - 1]


if __name__ == '__main__':
    my_obj = IterObj(1, 'lll', ['k, 5', (5, 6)], 4, {'f': 5}, InRange(5, 15).arguments)
    for i in my_obj:
        print(i)
