# -*- coding: utf-8 -*-
'''
Created on 2018-09-16

@author: Basel
'''

from app import stock_valuator as ev
from app import fx_data as fx
import matplotlib.pyplot as plt
from app.my_tushare import get_tushare

ts = get_tushare()

def plt_fx():
    sh50 = ts.get_k_data('000016', index=True, start='2017-07-01', end='2018-09-01')
    
    fx_rates = fx.get_cny_usd_fred('2017-01-01', '2018-09-01')
    
    fig, ax1 = plt.subplots()
    color = 'tab:red'
    ax1.set_xlabel('date')
    ax1.set_ylabel('volume', color=color)
    ax1.plot(sh50['date'], sh50['close'], color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('close', color=color)
    ax2.plot(fx_rates.index, fx_rates['Value'], color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    
    fig.tight_layout()
    
    
    plt.show()
    
if __name__ == '__main__':
    #print(get_ggm_price('000876.SZ', '20171231', required_return=0.1))
    #print(ev.get_ggm_price('000876.SZ', '20171231'))
    #print(get_ggm_price('000625.SZ', '20171231', required_return=0.11))
    print(ev.get_spm_price('000625.SZ', '20171231', 0.15))
    #print(fx.get_cny_usd_fred())
    #plt_fx()

