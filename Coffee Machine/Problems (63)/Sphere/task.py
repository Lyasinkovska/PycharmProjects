# create class Sphere here:
class Sphere:
	pi = 3.14

	def __init__(self, r):
		self.r = r
		self.v = round(4 * Sphere.pi * self.r ** 3 / 3, 2)


example_1 = Sphere(int(input()))
print(example_1.v)
