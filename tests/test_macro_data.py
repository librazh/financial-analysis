# -*- coding: utf-8 -*-
'''
Created on 2018-09-08

@author: Basel
'''
import unittest
import app.macro_data as md


class TestMacroData(unittest.TestCase):


    def test_get_deposit_rate(self):
        assert md.get_deposit_rate('定期存款整存整取(五年)', '20110407') == 0.0525


if __name__ == "__main__":
    unittest.main()