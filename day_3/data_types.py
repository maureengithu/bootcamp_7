def data_type(x):
	'''
	Takes an argument, x:
	-For an integer, return x ** 2
	- For a float, return x / 2
	- For a string, returns "Hello "+ x
	- For a boolean, return "boolean"
	- For a long, return squareroot(x)
	'''

	if type(x) == int:

		return x ** 2

	elif type (x) == float:

		return x / 2

	elif type (x) == str:

		return "Hello {}".format(x)

	elif type (x) == bool:

		return "boolean"

	elif type (x) == long:
		
		return "long"

	else:
		return "Check data type"

print data_type(12)
print data_type(12.9)
print data_type("Kenya")
print data_type(False)
print data_type(675**3563)