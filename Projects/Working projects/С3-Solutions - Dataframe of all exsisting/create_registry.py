import pandas as pd
import numpy as np
import openpyxl
import os
import const
import re

import func

"""
Создание БД из файла реестра
"""

with open('path.txt', encoding='UTF-8') as file:
    root_registry = str(file.readlines()[6])[:-1]
file.close()
data = pd.read_excel(root_registry) # Чтение реестра
registry = data[['№ КП','дата выдачи', 'Партнер (для КП)', 'Конечный заказчик', 'Дистрибьютор', 'Sale', 'Presale']]
registry = registry.fillna('Не указано')

