try:
	exception_test()
except AssertionError:
	print("AssertionError")
except ZeroDivisionError:
	print("ZeroDivisionError")
except ArithmeticError:
	print("ArithmeticError")
except Exception:
	print("Exception")
except BaseException:
	print("BaseException")
