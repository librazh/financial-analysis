# -*- coding: utf-8 -*-

import logging

import equity_data

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def get_spm_price(equity_code, report_period, required_return):
    """
    TODO:
    
    Sum of Perpetuities Method (SPM)
    
    P = E * G / K + D / K
    """

def get_ggm_price(equity_code, report_period, required_return):
    """
    Gordon Growth Model (GGM). It is a special case of Dividend Discount Model (DDM).
    
    P = D0 * (1 + g) / (r - g)
    
    where
        P: price
        D0: dividend        
        g: growth rate
        r: required return
    """
    d0 = equity_data.get_dividend_per_share(equity_code, report_period)
    g = get_growth_rate(equity_code, report_period)
    r = required_return
    price = d0 * (1 + g) / (r - g)
    return price

    
def get_growth_rate(equity_code, report_period):
    """
    growth rate = ROE * retention ratio
    """
    roe = get_roe(equity_code, report_period)
    retention_ratio = equity_data.get_retention_ratio(equity_code, report_period)
    growth_rate = roe * retention_ratio
    
    logger.debug('growth_rate=%s', growth_rate)
    return growth_rate


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
    print(get_ggm_price('000876.SZ', '20171231', 0.1))
    print(get_ggm_price('000625.SZ', '20171231', 0.11))
