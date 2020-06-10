"""
Program : test_coupon_calculations.py
Author : Chris Geralds
Date: 06/09/2020
This program tests coupon_calculations.
"""

import unittest
from Main.store import coupon_calculations as cc


class MyTestCase(unittest.TestCase):
    def test_price_under_ten(self):
        """"
        self.assertAlmostEqual(cc.calculate_order(9, 5, 10), 5.95, places=2)
        self.assertAlmostEqual(cc.calculate_order(4, 5, 15), 5.95, places=2)
        self.assertAlmostEqual(cc.calculate_order(9.95, 5, 20), 5.95, places=2)
        self.assertAlmostEqual(cc.calculate_order(7.13, 10, 10), 5.95, places=2)
        self.assertAlmostEqual(cc.calculate_order(10, 10, 15), 5.95, places=2)
        self.assertAlmostEqual(cc.calculate_order(10, 10, 20), 5.95, places=2)
        """
        # Next level of pricing  10 -30
        self.assertAlmostEqual(cc.calculate_order(35, 5, 10), 7.95, places=2)
        self.assertAlmostEqual(cc.calculate_order(20, 5, 15), 7.95, places=2)
        self.assertAlmostEqual(cc.calculate_order(29, 5, 20), 7.95, places=2)
        self.assertAlmostEqual(cc.calculate_order(39, 10, 10), 7.95, places=2)
        self.assertAlmostEqual(cc.calculate_order(30, 10, 15), 7.95, places=2)
        self.assertAlmostEqual(cc.calculate_order(25, 10, 20), 7.95, places=2)
        # Next 30 - 50 level
        self.assertAlmostEqual(cc.calculate_order(50, 5, 10), 11.95, places=2)
        self.assertAlmostEqual(cc.calculate_order(45, 5, 15), 7.95, places=2)
        self.assertAlmostEqual(cc.calculate_order(55, 5, 20), 7.95, places=2)
        self.assertAlmostEqual(cc.calculate_order(48, 10, 10), 7.95, places=2)

if __name__ == '__main__':
    unittest.main()
