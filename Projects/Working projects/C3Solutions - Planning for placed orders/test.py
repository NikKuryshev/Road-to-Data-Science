import re
import create_data
import func
import numpy as np
import const
import pandas as pd
d = {'Артикул': ['C3.RF4209', 'C3.UMM0020_3', 'C3.MM1620'], 'Кол-во': [1,2,3]}
dict = pd.DataFrame(d)
dict['Подкатегория'] = dict['Артикул'].str.rstrip('1234567890_')
dict['Категория'] = None
for key, values in const.categories.items():
    dict['Категория'] = np.where(dict['Подкатегория'].isin(values), key, dict['Категория'])

print(dict)