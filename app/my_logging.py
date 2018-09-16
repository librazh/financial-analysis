# -*- coding: utf-8 -*-
'''
Created on 2018-09-09

@author: Basel
'''

import logging.config
from config import default

def get_logger(name=None):
    logging.config.dictConfig(default.LOGGING_CONFIG)
    if name is None:
        name = 'financial-analysis'
    return logging.getLogger(name)