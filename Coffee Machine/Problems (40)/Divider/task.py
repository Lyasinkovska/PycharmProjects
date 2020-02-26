var = int(input())
if var % 7 == 0:
    print("7")
elif var % 5 == 0:
    print("5")
elif var % 3 == 0:
    print("3")
else:
    if var % 2 == 0:
        print("2")
    else:
        print("Nothing")