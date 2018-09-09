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
            'format': '%(asctime)s [%(levelname)s] %(name)s.%(funcName)s (%(lineno)d): %(message)s'
        },
    },
    'handlers': { 
        'default': { 
            'level': 'DEBUG',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': { 
        '': { 
            'handlers': ['default'],
            'level': 'DEBUG',
            'propagate': True
        },
    } 
}


def getLogger(name):
    logging.config.dictConfig(DEFAULT_CONFIG)
    return logging.getLogger(name)


class Logger(logging.Logger):
    '''
    TODO add entry function for logging the entry parameters
    '''

    def entry(self, *args):
        arg_dict = dict()
        for arg in args:
            arg_dict[arg.__name__] = arg
    
    def exit(self, *args):
        arg_dict = dict()
        for arg in args:
            arg_dict[arg.__name__] = arg
