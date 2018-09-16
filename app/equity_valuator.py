# -*- coding: utf-8 -*-

from . import equity_data as ed
from . import macro_data as md

from .my_logging import get_logger

logger = get_logger()


def get_spm_price(equity_code, report_period, required_return=None):
    '''
    Sum of Perpetuities Method (SPM)
    
    P = E * G / K**2 + D / K
    
    where
        P: price
        E: EPS
        G: growth rate
        K: required return, discount rate
        D: dividend per share
    '''
    
    e = ed.get_net_income(equity_code, report_period) / ed.get_total_share(equity_code, report_period)
    g = get_growth_rate(equity_code, report_period)
    if required_return is None:
        k = md.get_deposit_rate('定期存款整存整取(五年)')
    else:
        k = required_return

    d =ed.get_dividend_per_share(equity_code, report_period) 

    price = e * g / k**2 + d / k
    
    return price

def get_ggm_price(equity_code, report_period, required_return=None):
    '''
    Gordon Growth Model (GGM). It is a special case of Dividend Discount Model (DDM).
    
    P = D0 * (1 + g) / (r - g)
    
    where
        P: price
        D0: dividend        
        g: growth rate
        r: required return
    '''
    d0 = ed.get_dividend_per_share(equity_code, report_period)
    g = get_growth_rate(equity_code, report_period)
    
    if required_return is None:
        r = md.get_deposit_rate('定期存款整存整取(五年)')
    else:
        r = required_return
    price = d0 * (1 + g) / (r - g)
    return price

    
def get_growth_rate(equity_code, report_period):
    """
    growth rate = ROE * retention ratio
    """
    roe = get_roe(equity_code, report_period)
    retention_ratio = ed.get_retention_ratio(equity_code, report_period)
    growth_rate = roe * retention_ratio
    
    logger.debug('growth_rate=%s', growth_rate)
    return growth_rate


def get_dividend_growth_rate(equity_code, report_period):
    """
    TODO: Geometric mean of the dividend growth in each year
    """


def validate_dividend_growth_rate():
    """
    TODO: The dividend growth rate should not be much far away from GDP growth rate
    """


def get_roe(equity_code, report_period):
    net_income = ed.get_net_income(equity_code, report_period)
    total_equity = ed.get_total_equity(equity_code, report_period)
    roe = net_income / total_equity
    logger.debug('roe=%s', roe)
    return roe


def get_roa(equity_code, report_period):
    net_income = ed.get_net_income(equity_code, report_period)
    total_asset = ed.get_total_asset(equity_code, report_period)
    roa = net_income / total_asset
    logger.debug('roa=%s', roa)
    return roa
