import unittest
from store import  coupon_calculations

class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertAlmostEqual(5.95,(coupon_calculations(9, 5, 10)))
        self.assertAlmostEqual(5.95,(coupon_calculations(4, 5, 15)))
        self.assertAlmostEqual(5.95,(coupon_calculations(9.95, 5, 20)))
        self.assertAlmostEqual((5.95,(coupon_calculations(7.13, 10,10))))
        self.assertAlmostEqual((5.95,(coupon_calculations(-1, 10, 15))))
        self.assertAlmostEqual((5.95,(coupon_calculations(0, 10, 20))))



if __name__ == '__main__':
    unittest.main()
