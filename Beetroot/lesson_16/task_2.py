"""
Create your own implementation of a built-in function range, named in_range(), which takes three parameters:
`start`, `end`, and optional step. Tips: See the documentation for `range` function
"""


class InRange:
    def __init__(self, *args: int):
        self.arguments = args
        self.start = 0
        self.step = 1
        self.stop = None
        self.check_type()
        self.check_len_arguments()

    def check_type(self):
        if not any(isinstance(arg, int) for arg in self.arguments):
            raise TypeError('Must be integer')

    def check_len_arguments(self):
        if len(self.arguments) == 1 and self.arguments[0] > 0:
            self.stop = self.arguments[0]
        elif len(self.arguments) == 2 and self.arguments[0] < self.arguments[1]:
            self.start = self.arguments[0]
            self.stop = self.arguments[1]
        elif len(self.arguments) == 3 and (self.arguments[0] < self.arguments[1] and self.arguments[2] > 0) \
            or (len(self.arguments) == 3 and self.arguments[0] > self.arguments[1] and self.arguments[2] < 0):
            self.start = self.arguments[0]
            self.stop = self.arguments[1]
            self.step = self.arguments[2]
        elif self.step == 0:
            raise Exception('Step cannot be 0')
        else:
            raise Exception('Wrong arguments')

    def __next__(self):
        result = self.__iter__()
        for element in result:
            return element
        raise StopIteration

    def __iter__(self):
        self.start -= self.step
        self.stop -= self.step
        if self.start < self.stop:
            while self.start < self.stop:
                self.start += self.step
                yield self.start
        else:
            while self.start > self.stop:
                self.start += self.step
                yield self.start


if __name__ == '__main__':
    my = InRange()
    print(my.start, my.stop, my.step)
    for i in my:
        print(i)
