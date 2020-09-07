first = int(input())
second = int(input())

if first > second:
    print("The first one wins")
elif second > first:
    print("The second one wins")
else:
    print("Draw")

while True:
   number_one = int(input("Please, enter the first number: "))
   number_two = int(input("Please, enter the second number: "))
   try:
       result = number_one / number_two
   except ZeroDivisionError:
       print("We achieve it thanks to except ***You can not divide by zero!!")
   else:
       print("The result of your division is: ", result)
   finally:
       print("It is done through finally ***Thanks for using our calculator! Come again!")