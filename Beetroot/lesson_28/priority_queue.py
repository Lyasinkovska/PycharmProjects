from typing import List


class PriorityQueue:
    def __init__(self):
        self.__prior_queue: List[int] = [0]
        self.__size: int = 0

    @property
    def priority_queue(self):
        return self.__prior_queue

    @property
    def size(self):
        return self.__size

    def __perc_up(self, i) -> None:
        while i // 2 > 0:
            if self.__prior_queue[i] < self.__prior_queue[i // 2]:
                self.__prior_queue[i // 2], self.__prior_queue[i] = self.__prior_queue[i], self.__prior_queue[i // 2]
            i //= 2

    def __perc_down(self, i) -> None:
        while (i * 2) <= self.__size:
            mc = self.__min_child(i)
            if self.__prior_queue[i] > self.__prior_queue[mc]:
                self.__prior_queue[i], self.__prior_queue[mc] = self.__prior_queue[mc], self.__prior_queue[i]
            i = mc

    def __min_child(self, i) -> int:
        if i * 2 + 1 > self.__size:
            return i * 2
        if self.__prior_queue[i * 2] < self.__prior_queue[i * 2 + 1]:
            return i * 2
        else:
            return i * 2 + 1

    def enqueue(self, k) -> None:
        self.__prior_queue.append(k)
        self.__size += 1
        self.__perc_up(self.__size)

    def dequeue(self):
        ret_val = self.__prior_queue[1]
        self.__prior_queue[1] = self.__prior_queue[self.__size]
        self.__size -= 1
        self.__prior_queue.pop()
        self.__perc_down(1)
        return ret_val


if __name__ == '__main__':
    my_queue = PriorityQueue()
    my_queue.enqueue(20)
    my_queue.enqueue(2)
    my_queue.enqueue(25)
    my_queue.enqueue(1)
    my_queue.enqueue(13)
    my_queue.enqueue(3)
    print(my_queue.priority_queue)
    print(my_queue.dequeue())
    print(my_queue.size)
    print(my_queue.priority_queue)
