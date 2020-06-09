import unittest
from store import coupon_calculations

class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        self.assertAlmostEqual(coupon_calculations(9, 5, 10),5.95, places=2)
        self.assertAlmostEqual(coupon_calculations(4, 5, 15), 5.95,places=2)
        self.assertAlmostEqual(coupon_calculations(9.95, 5, 20),5.95,places=2)
        self.assertAlmostEqual(coupon_calculations(7.13, 10, 10),5.95,places=2)
        self.assertAlmostEqual(coupon_calculations(-1, 10, 15),5.95,places=2)
        self.assertAlmostEqual(coupon_calculations(0, 10, 20),5.95,places=2)



if __name__ == '__main__':
    unittest.main()
