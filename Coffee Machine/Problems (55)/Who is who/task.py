class Angel:
    color = "white"
    feature = "wings"
    home = "Heaven"


class Demon:
    color = "red"
    feature = "horns"
    home = "Hell"


# write your code here
check = input().split(' ')
if getattr(Angel, check[0]) == check[1]:
    print("Angel")
elif getattr(Demon, check[0]) == check[1]:
    print("Demon")
else:
    print("No match")
