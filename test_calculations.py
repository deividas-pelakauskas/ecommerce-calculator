import unittest
import ecommerce_calculator as calc


class TestCalc(unittest.TestCase):

    def test_ebay_profit(self):
        product = calc.Ebay(10, 5, 2)
        result = product.calculate_profit()
        self.assertEqual(result, 7.02)

    def test_ebay_fees(self):
        product = calc.Ebay(10, 5, 2)
        result = product.calculate_fees()
        self.assertEqual(result, 2.98)


if __name__ == "__main__":
    unittest.main()
