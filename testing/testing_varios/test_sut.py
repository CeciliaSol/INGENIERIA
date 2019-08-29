import unittest
import sut

class TestSut(unittest.TestCase):


	
	def tests_area(self):
		area = sut.area(3,2)
		self.assertTrue(area==6)
	
	def tests_saludar(self):
		nombre = sut.saludar('paola')
		self.assertTrue("Hola " + 'paola')
		
		
	
	
if __name__ == '__main__':
	unittest.main()
	
