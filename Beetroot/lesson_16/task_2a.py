class InRange:
    def __init__(self, start: int, stop: int, step: int = 1):
        self.__start = start
        self.__stop = stop
        self.__step = step
        self.__range = [item for item in self]

    @property
    def range(self):
        return self.__range

    def __iter__(self):
        return self

    def __next__(self):
        if (self.__step > 0 and self.__start >= self.__stop) or (self.__step < 0 and self.__start <= self.__stop):
            raise StopIteration
        if self.__step == 0:
            raise ValueError("Step cannot be 0")
        current = self.__start
        self.__start += self.__step
        return current

    def __contains__(self, item):
        return item in self.__range


if __name__ == '__main__':
    my_range = InRange(0, 12, 5)
    print(my_range.range)
    print(5 in my_range)
    print(2 in my_range)
