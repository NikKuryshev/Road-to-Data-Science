import pandas as pd
import numpy as np
import openpyxl
import os
import const
import re

import func

kp_number = [5747]
df = pd.DataFrame()
"""
Создание общей БД для заданного списка номеров КП
"""
list_of_paths = func.get_actual_kp_file(kp_number) # Получение списка путей к файлам по номерам КП
for path in list_of_paths: # Прогонка по путям
    list_of_offer = func.get_sheet(path) # Получение списка листов файла
    data = func.get_data(path, list_of_offer)
    data['Версия'] = re.findall(r'v\d{1,2}', path)# Чтение листа, получение БД
    df = pd.concat([df,data]).reset_index(drop = True) # Объединение данных каждого КП в одну общую базу
    #func.create_category(df)

"""
следующие две строки это вариант выдачи данных по сумме всех заказнных позиций
"""
sum_data = df.groupby('Артикул').agg(const.aggregation).reset_index() # Суммирование одинаковых артикулов
sum_data.drop(sum_data[sum_data['Количество'] == 0].index, inplace = True) # удаление нулевых количеств из базы данных
sum_data.sort_values(['Стоимость с проектной скидкой,\n  руб.','Количество'], ascending = False, inplace = True)

#func.create_file(final_data) #создание excel файла с БД
print(df.shape)

