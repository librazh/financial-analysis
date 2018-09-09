# -*- coding: utf-8 -*-
"""
TODO: Track and forecast indexes
"""
import my_tushare
import matplotlib.pyplot as plt
import my_logging


logger = my_logging.getLogger(__name__)

ts = my_tushare.get_tushare()

def demo(index_code):
    df = ts.get_k_data(index_code, index=True, start='2018-08-01', end='2018-08-16')
    
    fig, ax1 = plt.subplots()
    color = 'tab:red'
    ax1.set_xlabel('date')
    ax1.set_ylabel('volume', color=color)
    ax1.plot(df['date'], df['volume'], color=color)
    ax1.tick_params(axis='y', labelcolor=color)
    
    ax2 = ax1.twinx()
    color = 'tab:blue'
    ax2.set_ylabel('close', color=color)
    ax2.plot(df['date'], df['close'], color=color)
    ax2.tick_params(axis='y', labelcolor=color)
    
    fig.tight_layout()
    
    # plt.plot(df['date'], df['volume'], 'b-', df['date'], df['close'], 'r--')
    
    #plt.ylabel('index')
    #plt.xlabel('date')
    
    plt.show()

if __name__ == '__main__':
    demo('399006')
