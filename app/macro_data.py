# -*- coding: utf-8 -*-

from pandas import Period

import my_tushare
import my_logging

logger = my_logging.getLogger(__name__)

ts = my_tushare.get_tushare()


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
    
    df = ts.get_deposit_rate()
    df = df.sort_values(by=['date'])
    
    df = df.loc[df['deposit_type'] == deposit_type, ['date', 'rate']]
    
    logger.debug('df.values=\n%s', df.values)
    
    deposit_rate = None
    for record in df.values:
        rate_date = Period(record[0])
        if rate_date <= report_period and record[1] != '--':
            deposit_rate = float(record[1]) / 100

    logger.debug('deposit_rate=%f', deposit_rate)
    return deposit_rate


if __name__ == '__main__':
    print(get_deposit_rate('定期存款整存整取(五年)', '20110407'))
