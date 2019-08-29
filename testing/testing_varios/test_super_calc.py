import sut
import unittest
from unittest.mock import MagicMock
import math


class TestBase(unittest.TestCase):

	def test_supercalc(self):
		math.exp=MagicMock(return_value=2)
		math.sqrt=MagicMock(return_value=2)
		a = sut.supercal(3)
		self.assertTrue(a == 2)
		
if __name__ == '__main__':
    unittest.main()		
		
