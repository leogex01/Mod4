"""
Program :test_validation_with_try.py
Author : Chris Geralds
Date : 06/10/202
A test to check a raised value error on negatives for averaged test scores
"""

import unittest
from Main.input_validation import validation_with_try as vw

class MyTestCase(unittest.TestCase):
    def test_average_negative_exception(self):
        with self.assertRaises(ValueError):
            vw.average(-90, 89, 78)
            vw.average(90, -9, 45)
            vw.average(89, 10, -56)

    def test_average_string_exception(self):
        with self.assertRaises(ValueError):
            vw.average('som', 'e', 'string')




if __name__ == '__main__':
    unittest.main()
