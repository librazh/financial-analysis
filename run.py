# -*- coding: utf-8 -*-
'''
Created on 2018-09-16

@author: Basel
'''

from app import equity_valuator as ev

if __name__ == '__main__':
    #print(get_ggm_price('000876.SZ', '20171231', required_return=0.1))
    #print(ev.get_ggm_price('000876.SZ', '20171231'))
    #print(get_ggm_price('000625.SZ', '20171231', required_return=0.11))
    print(ev.get_spm_price('000876.SZ', '20171231', 0.1))
