import re
import func
import numpy as np
import const
import openpyxl
import pandas as pd

kp_number = [4925]
df = pd.DataFrame()

drop_item = ['C3.DI9999', 'C3.DI9998', 'C3.DL0000', 'C3.DL0001', 'C3.DL0002', 'C3.DL0003', 'C3.DL0004', \
	'C3.DL0005', 'C3.DL0006', 'C3.AD9999', 'C3.TP9999', 'C3.MM9999', 'C3.SP9999', 'C3.CX9999', 'C3.IX9999', 'C3.UP9999', \
	'C3.WARRANTY2Y', 'C3.WARRANTY3Y', 'C3.WARRANTY4Y', 'C3.WARRANTY5Y']
"""
Создание общей БД для заданного списка номеров КП
"""
kp_number = [5434, 4925]
df = pd.DataFrame()
"""
Создание общей БД для заданного списка номеров КП
"""
list_of_paths = func.get_actual_kp_file(kp_number) # Получение списка путей к файлам по номерам КП
for path in list_of_paths: # Прогонка по путям
    list_of_offer = func.get_sheet(path) # Получение списка листов файла


    data = pd.DataFrame()
    for sheet in list_of_offer:
        dict = pd.read_excel(path, sheet_name=sheet)  # Чтение КП по заданным столбцам, начиная с 14 строки
        location = dict[dict['Unnamed: 2'] == 'Артикул'].index

        dict = pd.read_excel(path, sheet_name=sheet, skiprows=location[0] + 1, usecols='C:K') # Чтение КП по заданным столбцам, начиная с 14 строки
        df = dict.dropna().loc[~dict['Артикул'].isin(drop_item)] # Удаление сервисных артикулов
        data = pd.concat([data,df]).reset_index(drop=True) # Объединение в общую базу данных, если есть несколько страниц в КП
        data['Дата выдачи КП'] = re.findall(r'\d{2}\.\d{2}\.\d{4}', path)[0]  # Добавление столбца с датой
        data['Номер КП'] = re.findall(r'\d{3,4}', path)[0]  # Добавление столбца с номером КП
    new = data

print(location[0])