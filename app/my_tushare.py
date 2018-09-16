'''
Created on 2018-09-08

@author: Basel
'''
import tushare as ts
from instance import config

def get_tushare():
    ts.set_token(config.TUSHARE_TOKEN)
    return ts