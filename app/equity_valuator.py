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

def get_rrr_capm(beta=None, rm=None):
    '''
    TODO:       
    Get required rate of return by Capital Asset Pricing Model (CAPM)
    rrr from CAPM = rf + beta(rm - rf)
    
    where
        rrr: required rate of return
        rf: Risk free rate
        beta: market risk
        rm: expected market return
    '''
    logger.debug('beta=%s, rm=%s', beta, rm)
    
    rf = md.get_deposit_rate('定期存款整存整取(五年)')
    
    if beta is None:
        beta = 1
    if rm is None:
        rm = 0.1
    
    rrr_from_capm = rf + beta * (rm - rf)
    
    logger.debug('rrr_from_capm=%s', rrr_from_capm)
    return rrr_from_capm

def get_rrr_wacc(equity_code, report_period):
    '''
    TODO:
    Get required rate of return using Weighted Average Cost of Capital (WACC)
    rrr from WACC = (total equity / total asset) * cost of equity + (total debt / total asset) * cost of debt * (1 - tax rate)
    '''
    
    logger.debug('equity_code=%s, report_period=%s', equity_code, report_period)
    
    total_asset = ed.get_total_asset(equity_code, report_period)
    total_equity = ed.get_total_equity(equity_code, report_period)
    total_debt = ed.get_total_debt(equity_code, report_period)
    
    # Tax rate in China is average 40%
    tax_rate = 0.4
    
    # TODO: Calculate cost of debt of the company. Here is using loan rate.
    cost_of_debt = md.get_loan_rate('中长期贷款(五年以上)', report_period)
    
    # TODO:Calculate cost of equity. Here is using dividend ratio.
    cost_of_equity = 1 - ed.get_retention_ratio(equity_code, report_period)
    
    rrr_from_wacc = (total_equity / total_asset) * cost_of_equity + (total_debt / total_asset) * cost_of_debt * (1 - tax_rate)
    
    logger.debug('rrr_from_wacc=%s', rrr_from_wacc)
    
    return rrr_from_wacc
    