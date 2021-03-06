# -*- coding: utf-8 -*-
"""
Note:
    * report_period: pandas.Period value
"""

import os

from pandas import Period
import pandas as pd

from .my_tushare import get_tushare
from .my_logging import get_logger

logger = get_logger()
ts = get_tushare()
pro = ts.pro_api()

dividend_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'data', 'dividend')
logger.debug('dividend_dir=%s', dividend_dir)


def get_total_share(equity_code, report_period):
    equity_data = pro.balancesheet(ts_code=equity_code, period=report_period)
    total_share = equity_data['total_share'][0]
    logger.debug('total_share=%s', total_share)
    return total_share


def get_net_income(equity_code, report_period):
    equity_data = pro.income(ts_code=equity_code, period=report_period)
    net_income = equity_data['n_income'][0]
    logger.debug('net_income=%s', net_income)
    return net_income


def get_retained_earning(equity_code, report_period):
    equity_data = pro.balancesheet(ts_code=equity_code, period=report_period)
    retained_earning = equity_data['undistr_porfit'][0]
    logger.debug('retained_earning=%s', retained_earning)
    return retained_earning 

    
def get_retention_ratio(equity_code, report_period):
    logger.debug('equity_code=%s, report_period=%s', equity_code, report_period)
    
    equity_data = pd.read_excel(os.path.join(dividend_dir, equity_code + '.xlsx'))
    equity_data = equity_data.loc[equity_data[u'年度'] == str(Period(report_period).end_time.date()), [u'收益留存率']]
    
    retention_ratio = equity_data.iloc[0][0]
    
    logger.debug('retention_ratio=%s', retention_ratio)
    return retention_ratio


def get_dividend_per_share(equity_code, report_period):
    logger.debug('equity_code=%s, report_period=%s', equity_code, report_period)
    
    equity_data = pd.read_excel(os.path.join(dividend_dir, equity_code + '.xlsx'))
    equity_data = equity_data.loc[equity_data[u'年度'] == str(Period(report_period).end_time.date()), [u'每股股利(元)']]
    
    dividend_per_share = equity_data.iloc[0][0]
    
    logger.debug('dividend_per_share=%s', dividend_per_share)
    return dividend_per_share


def get_retention_ratio_from_balance_sheet(equity_code, report_period):
    
    periods = pd.period_range(end=report_period, freq='Y', periods=2).end_time.strftime('%Y%m%d')
    logger.debug('periods=%s', periods)
    
    retained_earning_0 = get_retained_earning(equity_code, periods[0])
    retained_earning_1 = get_retained_earning(equity_code, periods[1])
    
    retained_earning = retained_earning_1 - retained_earning_0
    
    net_income = get_net_income(equity_code, report_period)
    retention_ratio = retained_earning / net_income
    logger.debug('retention_ratio=%s', retention_ratio)
    return retention_ratio

def get_total_debt(equity_code, report_period):
    
    logger.debug('equity_code=%s, report_period=%s', equity_code, report_period)
    df = pro.balancesheet(ts_code=equity_code, period=report_period)
    total_debt = df['total_liab'][0]
    logger.debug('total_debt=%f', total_debt)
    return total_debt

def get_total_equity(equity_code, report_period):
    logger.debug('equity_code=%s, report_period=%s', equity_code, report_period)
    df = pro.balancesheet(ts_code=equity_code, period=report_period)
    total_equity = df['total_hldr_eqy_inc_min_int'][0]
    logger.debug('total_equity=%f', total_equity)
    return total_equity
      
def get_total_asset(equity_code, report_period):
    logger.debug('equity_code=%s, report_period=%s', equity_code, report_period)
    df = pro.balancesheet(ts_code=equity_code, period=report_period)
    total_asset = df['total_assets'][0]
    logger.debug('total_asset=%f', total_asset)
    return total_asset

def get_tax_payable(equity_code, report_period):
    logger.debug('equity_code=%s, report_period=%s', equity_code, report_period)
    df = pro.balancesheet(ts_code=equity_code, period=report_period)
    tax_payable = df['taxes_payable'][0]
    logger.debug('tax_payable=%f', tax_payable)
    return tax_payable
