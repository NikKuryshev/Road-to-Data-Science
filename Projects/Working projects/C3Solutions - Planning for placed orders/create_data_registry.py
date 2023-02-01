import pandas as pd
import const
import create_registry
import func
import time
import re

start = time.time()

kp_number = []
for index, value in create_registry.reg.items():
    kp_number.append(value) # Создание списка номеров КП

df = pd.DataFrame()
"""
Создание общей БД для заданного списка номеров КП
"""
fail = []
list_of_paths = func.get_actual_kp_file(kp_number) # Получение списка путей к файлам по номерам КП
for path in list_of_paths: # Прогонка по путям
    try:
        list_of_offer = func.get_sheet(path) # Получение списка листов файла
        data = func.get_data(path, list_of_offer) # Чтение листа, получение БД
        first = re.findall('\d{4}\.', path)
        version = re.findall('\d{1,2}', path)[-1]
        if len(first) > 0:
            data['Версия'] = 1
        else:
            data['Версия'] = version
        df = pd.concat([df,data]).reset_index(drop = True) # Объединение данных каждого КП в одну общую базу
    except KeyError:
        fail.append(path+ ' KeyError')
    except IndexError:
        fail.append(path+' IndexError')
    except AttributeError:
        fail.append((path+' AttributeError'))
    except FileNotFoundError:
        fail.append(path+' FileNotFoundError')

"""
следующие две строки это вариант выдачи данных по сумме всех заказнных позиций
"""
#sum_data = df.groupby('Артикул').agg(const.aggregation).reset_index() # Суммирование одинаковых артикулов
#sum_data.drop(sum_data[sum_data['Количество'] == 0].index, inplace = True) # удаление нулевых количеств из базы данных
#sum_data.sort_values(['Стоимость с проектной скидкой,\n  руб.','Количество'], ascending = False, inplace = True)

#func.create_file(final_data) #создание excel файла с БД
end = time.time() - start
df.to_csv('data_2021_version_service.csv', sep=';', encoding='utf-8')
print(df.shape)
with open ('output.txt', 'w') as f:
    for line in fail:
        f.write(line + '\n')
print(df.shape)