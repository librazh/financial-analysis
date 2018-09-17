# -*- coding: utf-8 -*-
'''
Created on 2018-09-15

@author: Basel
'''
import requests
import quandl
from instance import config


def get_cny_usd_boc():
    payload = {
        'app': 'finance.rate_cnyquot_history',
        'curno': 'USD',
        'bankno': 'BOC',
        'date': '20161101',
        'appkey': config.NOWAPI_APPKEY,
        'sign': config.NOWAPI_SIGN,
        'format': 'json',
    }
    
    r = requests.get('http://api.k780.com', params=payload)
    
    return r.json()

def get_cny_usd_fred(start_date=None, end_date=None):
    quandl.ApiConfig.api_key = config.QUANDL_APPKEY
    rates = quandl.get('FRED/DEXCHUS', start_date=start_date, end_date=end_date)
    return rates
