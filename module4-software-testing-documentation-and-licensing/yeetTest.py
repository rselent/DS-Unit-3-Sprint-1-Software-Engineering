"""
Simple test case for yeetroot.py
"""

from yeetroot import yeetRoot
import unittest

class yeetTests( unittest.TestCase):
	"""
	obligatory docstring, compulsory, tests square yeet function
	that tests whether you're yeeting numbers correctly
	"""

	def test_yeet( self):
		print( self.assertNotEqual( yeetRoot(), 12))
		print( __name__)

# test = yeetTests().test_yeet()

# print( test)

if __name__ == '__main__':
	unittest.main()


