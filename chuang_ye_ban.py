# -*- coding: utf-8 -*-

import tushare as ts
import matplotlib.pyplot as plt

ts.set_token('6637031d14f4036a8dfffe9b186ff41164ddc1d2c9f6c5b521aaa56f')

df = ts.get_k_data('399006', index=True, start='2018-08-01', end='2018-08-16')

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



