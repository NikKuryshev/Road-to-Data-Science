import re
import create_data
import func
import const


data = create_data.df

data['Категория'] = data['Артикул'].str.f
print(data.shape)
