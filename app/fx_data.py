# -*- coding: utf-8 -*-
'''
Created on 2018-09-15

@author: Basel
'''
import requests
from instance import config


def get_cny_usd():
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

if __name__ == '__main__':
    
    print(get_cny_usd()['result']['lists'][0]['middle'])
