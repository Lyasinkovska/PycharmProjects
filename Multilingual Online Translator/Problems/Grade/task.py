#  Posted from EduTools plugin
grade = int(input())
maximum = int(input())
result = grade/maximum*100
if result < 60:
	print("F")
elif 60 <= result < 70:
	print("D")
elif 70 <= result < 80:
	print("C")
elif 80 <= result < 90:
	print("B")
elif 90 <= result <= 100:
	print("A")
