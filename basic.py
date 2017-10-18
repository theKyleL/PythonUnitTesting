"""
This file contains basic python functions for use with the test_basic.py unit test example file.
"""

def basic_addition(a, b):
	"""
	Return the sum of the two arguments
	a + b
	"""
	return a + b


def basic_subtraction(a, b):
	"""
	Return the difference of the two arguments
	a - b
	"""
	return a - b


def basic_multiplication(a, b):
	"""
	Return the product of the two arguments
	a * b
	"""
	return a * b


def basic_division(a, b):
	"""
	Return the quotient of the two arguments
	a / b
	"""
	if b == 0:
		raise ValueError('Division by 0!')
	return float(a) / float(b)


def concatinateStuff(a, b):
	"""
	Return the concatinated value
	"""
	return '{}{}'.format(a, b)
