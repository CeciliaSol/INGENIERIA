import sut
import unittest
from unittest.mock import MagicMock

class TestBase(unittest.TestCase):

	def test_supercalc(self):
		sut.exp=MagicMock(return_value=2)
		sut.sqrt=MagicMock(return_value=2)
		a = calculos.calcula(5)
		
if __name__ == '__main__':
    unittest.main()		
		
