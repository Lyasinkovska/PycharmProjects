class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = int(hyp)
        self.a = int(leg_1)
        self.b = int(leg_2)
        # calculate the area here
        self.area = (self.a * self.b / 2 if self.c ** 2 == self.a ** 2 + self.b ** 2 else "Not right")


side = input().split()
area_triangle = RightTriangle(side[0], side[1], side[2])
print(area_triangle.area)
