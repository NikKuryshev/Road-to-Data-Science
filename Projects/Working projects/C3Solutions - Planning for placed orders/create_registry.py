import pandas as pd

"""
Создание БД из файла реестра
"""

with open('path.txt', encoding='UTF-8') as file:
    root_registry = str(file.readlines()[6])[:-1]
file.close()
data = pd.read_excel(root_registry) # Чтение реестра
registry = data[['№ КП','дата выдачи', 'Партнер (для КП)', 'Конечный заказчик', 'Дистрибьютор', 'Sale', 'Presale']]
registry = registry.fillna('Не указано')

registry_final = registry[registry['Presale'] != 'Тугаев']
reg = registry_final['№ КП']
print(reg.shape)
