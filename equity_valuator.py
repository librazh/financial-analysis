# -*- coding: utf-8 -*-

import logging
import pandas

import equity_data

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


def get_ggm_price(equity_code):
    """
    Gordon Growth Model (GGM). It is a special case of Dividend Discount Model (DDM).
    
    P = D0 * (1 + g) / (r - g)
    
    where
        P: price
        D0: dividend        
        g: growth rate
        r: required return
    """

    
def get_growth_rate(equity_code):
    """
    growth rate = ROE * retention ratio
    """


def get_roe(equity_code, report_period):
    net_income = equity_data.get_net_income(equity_code, report_period)
    total_equity = equity_data.get_total_equity(equity_code, report_period)
    roe = net_income / total_equity
    logger.debug('roe=%s', roe)
    return roe


def get_roa(equity_code, report_period):
    net_income = equity_data.get_net_income(equity_code, report_period)
    total_asset = equity_data.get_total_asset(equity_code, report_period)
    roa = net_income / total_asset
    logger.debug('roa=%s', roa)
    return roa


if __name__ == '__main__':
    print(get_roa('000876.SZ', '2017-12'))
