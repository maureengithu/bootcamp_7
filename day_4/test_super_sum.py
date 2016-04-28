''''
Test suit for super sum
'''
from unittest import TestCase
from super_sum import super_sum


class SuperSumTestCase(TestCase):     #Test Case for super sum.
	
	def test_empty_input(self):       #Test empty input.
		self.assertEqual(super_sum(), 0)

	def test_sum_of_integers(self):   #Test sum of integers.
		self.assertEqual(super_sum(1 ,2, 3), 6)
		self.assertEqual(super_sum(-1, 1), 0)
		self.assertNotEqual(super_sum(10, 10, 30), 100)

	def test_string_input_returns(self):   #Test string input to return 0.
		self.assertEqual(super_sum("string", 1, 4), 0)

	def test_sum_of_items_in_one_list(self): #Test sum ofitems in a single list.
		self.assertEqual(super_sum([1, 2, 3]), 6)