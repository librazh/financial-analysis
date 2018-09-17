# -*- coding: utf-8 -*-
'''
Created on 2018-09-16

@author: Basel
'''

from app import equity_valuator as ev
from app import fx_data as fx
import matplotlib.pyplot as plt

def plt_fx():
    fx_rates = fx.get_cny_usd_fred('2017-01-01', '2018-09-01')
    plt.plot(fx_rates.index, fx_rates['Value'])
    plt.show()
    
if __name__ == '__main__':
    #print(get_ggm_price('000876.SZ', '20171231', required_return=0.1))
    #print(ev.get_ggm_price('000876.SZ', '20171231'))
    #print(get_ggm_price('000625.SZ', '20171231', required_return=0.11))
    #print(ev.get_spm_price('000876.SZ', '20171231', 0.1))
    #print(fx.get_cny_usd_fred())
    plt_fx()

