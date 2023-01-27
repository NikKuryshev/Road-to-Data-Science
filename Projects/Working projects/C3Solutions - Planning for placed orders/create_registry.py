import pandas as pd

"""
Создание БД из файла реестра
"""

with open('path.txt', encoding='UTF-8') as file:
    root_registry = str(file.readlines()[6])[:-1]
file.close()
data = pd.read_excel(root_registry, date_parser='дата выдачи', na_values='Не указано') # Чтение реестра
data = data[['№ КП','дата выдачи', 'Партнер (для КП)', 'Конечный заказчик', 'Дистрибьютор', 'Sale', 'Presale']]
registry = data[data['дата выдачи']>"2021"]
registry.to_csv('registry_2021.csv', sep=';')
registry_final = registry[registry['Presale'] != 'Тугаев']
reg = registry_final['№ КП'].astype('int32')
print(reg.shape)
