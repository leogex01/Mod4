import unittest
from Main.input_validation import validation_with_try as vw

class MyTestCase(unittest.TestCase):
    def test_average_negative_exception(self):
        with self.assertRaises(ValueError):
            vw.average(-90, 89, 78)





if __name__ == '__main__':
    unittest.main()
