import unittest
from pandas import *

from backtesting.Market import Market

class MarketTest(unittest.TestCase):
    def setUp(self):
        self.market = Market(["GOOG"],"2011-01-01","2011-01-30")
        self.market.load_historical_data()

    def test_get_stock_price(self):
        self.assertEqual(self.market.get_stock_price("GOOG","2011-01-10","close"),614.21)
        self.assertEqual(self.market.get_stock_price("GOOG","2011-01-10","actual_close"),614.21)
        self.assertEqual(self.market.get_stock_price("GOOG","2011-01-10","open"),614.80)
        self.assertEqual(self.market.get_stock_price("GOOG","2011-01-10","high"),615.39)
        self.assertEqual(self.market.get_stock_price("GOOG","2011-01-10","low"),608.56)


if __name__ == '__main__':
    unittest.main()