# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 23:16:00 2021

@author: garvi
"""


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dates = ['Nov 24 2020', 'Nov 23 2020', 'Nov 23 2020', 'Nov 23 2020', 'Nov 22 2020', 'Nov 22 2020', 'Nov 22 2020', 'Nov 22 2020', 'Nov 22 2020', 'Nov 22 2020', 'Nov 21 2020', 'Nov 21 2020', 'Nov 21 2020', 'Nov 21 2020', 'Nov 21 2020', 'Nov 21 2020', 'Nov 21 2020', 'Nov 20 2020', 'Nov 20 2020', 'Nov 20 2020', 'Nov 20 2020', 'Nov 20 2020', 'Nov 17 2020', 'Nov 17 2020', 'Aug 23 2020', 'Aug 23 2020', 'Aug 23 2020', 'Aug 23 2020', 'Nov 14 2020', 'Nov 14 2020', 'Nov 14 2020', 'Nov 14 2020', 'Nov 14 2020', 'Nov 14 2020', 'Nov 14 2020', 'Nov 14 2020', 'Nov 14 2020', 'Nov 13 2020', 'Nov 13 2020', 'Nov 13 2020', 'Nov 13 2020', 'Nov 13 2020', 'Nov 13 2020', 'Nov 12 2020', 'Nov 10 2020', 'Nov 9 2020', 'Nov 8 2020', 'Nov 7 2020']

import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame({'freq': dates})

df.groupby('freq', as_index=True).size().sort_values().plot(kind='bar', orientation='vertical')

plt.xlabel("The Days")
plt.ylabel("Frequency/Number of Days")
plt.title("Frequency of Days Showed")
plt.tight_layout()

plt.show()


import seaborn as sns
from collections import Counter

counter = Counter(dates)
df_new = pd.DataFrame.from_dict(counter, orient='index').reset_index()


g = sns.scatterplot(x = 'index', y = 0, data = df_new)
g.set_xticklabels(rotation=90, labels = df_new['index'])
plt.tight_layout()

plt.show()



    