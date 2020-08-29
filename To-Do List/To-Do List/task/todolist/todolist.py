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
    deadline = input("Enter deadline\n")
    new_row = Table(task=f'{new_task}', deadline=datetime.strptime(deadline,'%Y-%m-%d'))
    session.add(new_row)
    session.commit()
    print("The task has been added!\n")


def print_today_tasks():
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
        print(f"\n{next_day.strftime ('%A')} {next_day.day} {next_day.strftime ('%b')}:")
        records = session.query(Table).filter(Table.deadline == next_day).all()
        if records:
            for i in range(len(records)):
                print(f'{i + 1}. {records[i]}')
        else:
            print("Nothing to do!")


def print_all_tasks():
    all_tasks = session.query(Table).order_by(Table.deadline).all()
    deadlines = session.query(Table.deadline).order_by(Table.deadline).all()
    if all_tasks:
        for i in range(len(all_tasks)):
            print(f'{i+1}. {all_tasks[i]}. {deadlines[i].deadline.day} {deadlines[i].deadline.strftime("%b")}')
    else:
        print ("Nothing to do!")


def missed_tasks():

    rows = session.query(Table).filter(Table.deadline < datetime.today().date()).order_by(Table.deadline).all()
    deadlines = session.query(Table.deadline).filter(Table.deadline < datetime.today().date()).order_by(Table.deadline).all()
    if rows == []:
        print("Nothing is missed!")
    else:
        for i in range(len(rows)):
            print(f"{i+1}. {rows[i]}. {deadlines[i].deadline.day} {deadlines[i].deadline.strftime('%b')}")


def delete_task():
    print("Choose the number of the task you want to delete:\n")
    missed_tasks()
    action = int(input())
    rows = session.query(Table).filter(Table.deadline <= datetime.today().date()).order_by(Table.deadline).all()
    if rows != []:
        session.delete(rows[action-1])
        session.commit()
    print("The task has been deleted!")


while True:
    action = input("\n1) Today's tasks\n2) Week's tasks\n3) All tasks\n"
                   "4) Missed tasks\n5) Add task\n6) Delete task\n0) Exit\n")
    if action == "1":
        print_today_tasks()
    elif action == "2":
        print_week_tasks()
    elif action == "3":
        print_all_tasks()
    elif action == "4":
        print ("Missed tasks:")
        missed_tasks()
    elif action == "5":
        add_new_task()
    elif action == "6":
        delete_task()
    elif action == "0":
        print("Bye!")
        break

