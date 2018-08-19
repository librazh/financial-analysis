# -*- coding: utf-8 -*-
"""
Note:
    * report_period: pandas.Period value
"""

import logging
import pandas

import tushare as ts

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

ts.set_token('6637031d14f4036a8dfffe9b186ff41164ddc1d2c9f6c5b521aaa56f')
pro = ts.pro_api()


def get_total_share(equity_code, report_period):    
    global pro
    equity_data = pro.balancesheet(ts_code=equity_code, period=report_period)
    total_share = equity_data['total_share'][0]
    logger.debug('total_share=%s', total_share)
    return total_share


def get_net_income(equity_code, report_period):
    global pro
    equity_data = pro.income(ts_code=equity_code, report_period=report_period)
    net_income = equity_data['n_income'][0]
    logger.debug('net_income=%s', net_income)
    return net_income


def get_total_asset(equity_code, report_period):
    global pro
    equity_data = pro.balancesheet(ts_code=equity_code, period=report_period)
    total_asset = equity_data['total_assets'][0]
    logger.debug('total_asset=%s', total_asset)
    return total_asset


def get_total_equity(equity_code, report_period):
    global pro
    equity_data = pro.balancesheet(ts_code=equity_code, period=report_period)
    total_equity = equity_data['total_hldr_eqy_inc_min_int'][0]
    logger.debug('total_equity=%s', total_equity)
    return total_equity


def get_retained_earning(equity_code, report_period):
    global pro
    equity_data = pro.balancesheet(ts_code=equity_code, report_period=report_period)
    retained_earning = equity_data['undistr_porfit'][0]
    logger.debug('retained_earning=%s', retained_earning)
    return retained_earning 

    
def get_retention_ratio(equity_code, report_period):
    
    """
    TODO: fix
    """
    
    periods = pandas.period_range(end=report_period, freq='Y', periods=2)
    logger.debug('periods[0]=%s', periods[0])
    logger.debug('periods[1]=%s', periods[1])
    retained_earning1 = get_retained_earning(equity_code, str(periods[0]))
    retained_earning2 = get_retained_earning(equity_code, str(periods[1]))
    
    retained_earning = retained_earning1 - retained_earning2
    
    net_income = get_net_income(equity_code, report_period)
    retention_ratio = retained_earning / net_income
    logger.debug('retention_ratio=%s', retention_ratio)
    return retention_ratio


if __name__ == '__main__':
    print(get_retained_earning('000876.SZ', '2017-12'))
    print(get_retained_earning('000876.SZ', '2012-12'))
