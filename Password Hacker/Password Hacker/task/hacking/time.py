import datetime
start = datetime.datetime.now()
finish = datetime.datetime.now()
diff = finish - start
#delta = datetime.timedelta(seconds=1).total_seconds()
print(diff.seconds > 0.1)
#print(datetime.timedelta(seconds=1).total_seconds() > diff.microseconds/60)