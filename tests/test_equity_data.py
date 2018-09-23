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
        
    def test_get_total_debt(self):
        assert ed.get_total_debt('000876.SZ', '20171231') == 16216932626.25

    def test_get_total_equity(self):
        assert ed.get_total_equity('000876.SZ', '20171231') == 26234700397.73

    def test_get_total_asset(self):
        assert ed.get_total_asset('000876.SZ', '20171231') == 42451633023.980003

    def test_get_tax_payable(self):
        assert ed.get_tax_payable('000876.SZ', '20171231') == 185482124.76

if __name__ == "__main__":
    unittest.main()