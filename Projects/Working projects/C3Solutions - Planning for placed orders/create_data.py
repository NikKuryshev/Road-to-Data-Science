import pandas as pd
import numpy as np
import openpyxl
import os
import const
import re

import func

kp_number = [4679, 5486, 5612, 4087, 5411]
df = pd.DataFrame()
"""
Создание общей БД для заданного списка номеров КП
"""
list_of_paths = func.get_actual_kp_file(kp_number)
for path in list_of_paths:
    list_of_offer = func.get_sheet(path)
    data = func.get_data(path, list_of_offer)




    df = pd.concat([df,data]).reset_index(drop = True) # Объединение данных каждого КП в одну общую базу
#final_data = df.groupby('Артикул').agg(const.aggregation).reset_index() # Суммирование одинаковых артикулов
#final_data.drop(final_data[final_data['Количество'] == 0].index, inplace = True) # удаление нулевых количеств из базы данных

#func.create_file(final_data) #создание excel файла с БД
print(df.shape)

