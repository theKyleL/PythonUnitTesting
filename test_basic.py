"""
Example unit tests in python

UnitTest documentation can be found on the Python Software Foundation website at: 
https://docs.python.org/3/library/unittest.html?highlight=testcase
"""
import unittest # add various assert statements
import basic # file to be tested


class TestBasic(unittest.TestCase):


	def test_basic_addition(self):
		self.assertEqual(basic.basic_addition(4, 5), 9)
		self.assertEqual(basic.basic_addition(-1, 5), 4)
		self.assertEqual(basic.basic_addition(-40, 40), 0)
		self.assertEqual(basic.basic_addition(0, 4), 4)


	def test_basic_subtraction(self):
		self.assertEqual(basic.basic_subtraction(4, 5), -1)
		self.assertEqual(basic.basic_subtraction(-1, 5), -6)
		self.assertEqual(basic.basic_subtraction(-40, 40), -80)
		self.assertEqual(basic.basic_subtraction(0, 4), -4)


	def test_basic_multiplication(self):
		self.assertEqual(basic.basic_multiplication(0, 4), 0)
		self.assertEqual(basic.basic_multiplication(4, 5), 20)
		self.assertEqual(basic.basic_multiplication(-4, 5), -20)
		self.assertEqual(basic.basic_multiplication(-4, -5), 20)


	def test_basic_division(self):
		self.assertEqual(basic.basic_division(8, 4), 2)
		self.assertEqual(basic.basic_division(5, 2), 2.5)

		self.assertRaises(ValueError, basic.basic_division, 4, 0) 
		# note that function arguments are passed to the 'assertRaises' function

		# another method for testing exception handling
		with self.assertRaises(ValueError):
			basic.basic_division(4, 0)


	def test_concatination(self):
		self.assertEqual(basic.concatinateStuff('a', 'b'), 'ab')
		self.assertEqual(basic.concatinateStuff(4, 5), '45')


if __name__ == '__main__':
	unittest.main()
