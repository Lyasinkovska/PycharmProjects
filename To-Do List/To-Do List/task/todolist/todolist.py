from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
from datetime import datetime
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
    new_row = Table(task=f'{new_task}')
    session.add(new_row)
    session.commit ()
    print ("The task has been added!\n")

def print_todays_tasks():
    records = session.query (Table).all ()
    print ("Today:")
    if records:
        for i in range (len (records)):
            print (f'{i + 1}. {records[i]}')
    else:
        print ("Nothing to do!\n")

while True:
    action = input("1) Today's tasks\n2) Add task\n0) Exit\n")
    if action == "1":
        print_todays_tasks()
    elif action == "2":
        add_new_task()
    elif action == "0":
        break