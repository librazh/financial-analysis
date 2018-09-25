# -*- coding: utf-8 -*-
'''
Created on 2018-09-23

@author: Basel
'''
import unittest
import app.stock_valuator as ev


class TestEquityValuator(unittest.TestCase):


    def test_get_rrr_wacc(self):
        rrr_wacc = ev.get_rrr_wacc('000876.SZ', '20171231')
        assert rrr_wacc == 0.18266161174911283

        rrr_wacc = ev.get_rrr_wacc('000625.SZ', '20171231')
        assert rrr_wacc == 0.15046731447070782

if __name__ == "__main__":
    unittest.main()