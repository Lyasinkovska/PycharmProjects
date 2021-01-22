"""
Implement 2 classes, the first one is the Boss and the second one is the Worker.
Worker has a property 'boss', and its value must be an instance of Boss.
You can reassign this value, but you should check whether the new value is Boss. Each Boss has a list of his own
workers. You should implement a method that allows you to add workers to a Boss. You're not allowed to add instances
of Boss class to workers list directly via access to attribute, use getters and setters instead!
You can refactor the existing code.

id_ - is just a random unique integer

"""


class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    @property
    def workers(self):
        return self._workers

    @workers.setter
    def workers(self, worker):
        if isinstance(worker, Worker) and worker not in self.workers:
            worker.boss = self
            self._workers.append(worker)

    def __str__(self):
        return f'{self.name, self.company}'

    def __repr__(self):
        return self.__str__()


class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self._boss = boss

    @property
    def boss(self):
        return self._boss

    @boss.setter
    def boss(self, new_boss: Boss):
        if isinstance(new_boss, Boss) and self not in new_boss.workers:
            self._boss = new_boss
        else:
            raise Exception(f"{self.name} is already in {new_boss.name} workers list.")

    @boss.deleter
    def boss(self):
        del self.boss

    def __eq__(self, other):
        if not isinstance(other, Worker):
            return NotImplementedError
        return self.id == other.id and self.name == other.name and self.company == other.company and self.boss == other.boss

    def __str__(self):
        return f'{self.name}: {self.company}, {self.boss}'

    def __repr__(self):
        return self.__str__()


if __name__ == '__main__':
    b = Boss(1, 'Olena Teliga', 'SoftServe')
    b2 = Boss(2, 'Ivan Ivanov', 'EPAM')
    w1 = Worker(1, 'Liudmyla Yasinkovska', 'SoftServe', b)
    b.workers = w1
    w2 = Worker(2, 'Oksana Braun', 'EPAM', b)
    b.workers = w2
    print(b.workers, b)
    b2.workers = w2
    print(b2.workers, b2)
    w2.boss = b
    print(b.workers, b)
    print(b2.workers, b2)

