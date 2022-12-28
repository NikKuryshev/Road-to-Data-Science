import re
import create_data
import func
import const
import pandas as pd
d = {'Артикул': ['C3.RF4209', 'C3.UMM0020_3', 'C3.MM1620'], 'Кол-во': [1,2,3]}
dict = pd.DataFrame(d)
dict['Подкатегория'] = dict['Артикул'].str.rstrip('1234567890_')
for key, values in const.categories.items():
    for value in values:
        dict['Категория'] = dict['Подкатегория'].str.contains(value)

print(dict)