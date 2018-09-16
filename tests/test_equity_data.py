# -*- coding: utf-8 -*-
'''
Created on 2018-09-08

@author: Basel
'''
import unittest
import app.equity_data as ed

class TestEquityData(unittest.TestCase):


    def test_get_dividend_per_share(self):
        assert ed.get_dividend_per_share('000876.SZ', '20171231') == 0.15

    def test_get_retention_ratio(self):
        assert ed.get_retention_ratio('000876.SZ', '20171231') == 0.7226

if __name__ == "__main__":
    unittest.main()