from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime, timedelta
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///todo.db?check_same_thread=False')
Base = declarative_base()


class Table(Base):
    __tablename__ = 'task'
    id = Column(Integer, primary_key=True)
    task = Column(String, default='default_value')
    deadline = Column(Date, default=datetime.today())

    def __repr__(self):
        return self.task

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

def add_new_task():
    new_task = input("Enter task\n")
    deadline = input ("Enter deadline\n")
    new_row = Table(task=f'{new_task}', deadline=datetime.strptime(deadline,'%Y-%m-%d'))
    session.add(new_row)
    session.commit()
    print("The task has been added!\n")

def print_todays_tasks():
    records = session.query(Table).all()
    print(f"Today {datetime.today().day} {datetime.today().strftime('%b')}:")
    if records:
        for i in range(len(records)):
            print(f'{i + 1}. {records[i]}')
    else:
        print("Nothing to do!\n")

def print_week_tasks():
    for day in range(7):
        next_day = (datetime.today() + timedelta(days=day)).date()
        print(f"{next_day.strftime ('%A')} {next_day.day} {next_day.strftime ('%b')}:")
        records = session.query(Table).filter(Table.deadline == next_day).all()
        if records:
            for i in range (len (records)):
                print (f'{i + 1}. {records[i]}')
        else:
            print ("Nothing to do!\n")


def print_all_tasks():
    pass

while True:
    action = input("1) Today's tasks\n2) Week's tasks\n3) All tasks\n4) Add task\n0) Exit\n")
    if action == "1":
        print_todays_tasks()
    elif action == "2":
        print_week_tasks()
    elif action == "3":
        print_all_tasks()
    elif action == "4":
        add_new_task()
    elif action == "0":
        break

