# -*- coding: utf-8 -*-
'''
Created on 2018-09-09

@author: Basel
'''

import logging.config

DEFAULT_CONFIG = {
     
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': { 
        'standard': { 
            'format': '%(asctime)s [%(levelname)s] %(name)s.%(module)s.%(funcName)s (%(lineno)d): %(message)s'
        },
    },
    'handlers': { 
        'console': { 
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
        'file': { 
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': 'app.log',
        },
    },
    'loggers': { 
        '': { 
            'handlers': ['console', 'file'],
            'level': 'DEBUG',
            'propagate': True
        },
    } 
}


def getLogger(name=None):
    logging.config.dictConfig(DEFAULT_CONFIG)
    if name is None:
        name = 'financial-analysis'
    return logging.getLogger(name)