import re
import func
import numpy as np
import const
import openpyxl
import pandas as pd

kp_number = [5434]
df = pd.DataFrame()
"""
Создание общей БД для заданного списка номеров КП
"""

list_of_paths = ['C:\\Users\\nkuryshev\\YandexDisk\\C3 Presale\\=КП\\ИНЖИКОМ\\5434\\Offer C3 Solutions 5434 engicom 17.11.2022 v2.xlsx']
for path in list_of_paths: # Прогонка по путям
    wb = openpyxl.load_workbook(path, read_only=True)
    offer = []
    for sheet in wb:
        if 'offer' in sheet.title:
            offer.append(sheet.title)
    list_of_offer = offer
    wb.close()

    data = pd.DataFrame()
    for sheet in list_of_offer:
        dict = pd.read_excel(path, sheet_name=sheet)  # Чтение КП по заданным столбцам, начиная с 14 строки
        location = dict[dict['Unnamed: 2'] == 'Артикул'].index
print(location[0])