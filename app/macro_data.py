# -*- coding: utf-8 -*-

from pandas import Period

from .my_logging import get_logger
from .my_tushare import get_tushare

logger = get_logger()
ts = get_tushare()


def get_gdp(report_period):
    """
    TODO: Get GDP data
    """


def get_deposit_rate(deposit_type, report_period=None):
    
    logger.debug('deposit_type=%s, report_period=%s', deposit_type, report_period)

    if report_period is None:
        report_period = Period.now('D')   
    elif isinstance(report_period, str):
        report_period = Period(report_period)
    
    deposit_rates = ts.get_deposit_rate()
    deposit_rates = deposit_rates.sort_values(by=['date'])
    
    deposit_rates = deposit_rates.loc[deposit_rates['deposit_type'] == deposit_type, ['date', 'rate']]
    
    logger.debug('deposit_rates.values=\n%s', deposit_rates.values)
    
    deposit_rate = None
    for record in deposit_rates.values:
        rate_date = Period(record[0])
        if rate_date <= report_period and record[1] != '--':
            deposit_rate = float(record[1]) / 100

    logger.debug('deposit_rate=%f', deposit_rate)
    return deposit_rate

def get_loan_rate(loan_type, report_period=None):
    
    logger.debug('loan_type=%s, report_period=%s', loan_type, report_period)

    if report_period is None:
        report_period = Period.now('D')   
    elif isinstance(report_period, str):
        report_period = Period(report_period)
    
    loan_rates = ts.get_loan_rate()
    loan_rates = loan_rates.sort_values(by=['date'])
    
    loan_rates = loan_rates.loc[loan_rates['loan_type'] == loan_type, ['date', 'rate']]
    
    logger.debug('loan_rates.values=\n%s', loan_rates.values)
    
    loan_rate = None
    for record in loan_rates.values:
        rate_date = Period(record[0])
        if rate_date <= report_period and record[1] != '--':
            loan_rate = float(record[1]) / 100

    logger.debug('loan_rate=%f', loan_rate)
    return loan_rate


def get_shibor():
    df = ts.shibor_data()
    return df
