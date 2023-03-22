# Импорт библиотек
import pandas as pd
import matplotlib as plt
import seaborn as sns
import numpy as np

# Чтение сформированной базы данных (Без учета Тугаева)
df = pd.read_csv("data_2021_version_service.csv", sep=';', encoding='utf-8')
reg = pd.read_csv("registry.csv", sep='\t', encoding='utf-8')
rega = reg.rename(columns = {'№ КП':'kp_number', 'дата выдачи':'start_date', 'Партнер (для КП)':'partner', 'Конечный заказчик':'customer','Дистрибьютор':'distr','Sale.1':'sale','Presale':'presale'})

col = ['Артикул','Наименование','Количество','Цена для конечного пользователя, руб.','Стоимость для конечного пользователя, руб.','Дата выдачи КП','Номер КП','Проектная скидка','Цена с проектной скидкой,\n  руб.','Стоимость с проектной скидкой,\n  руб.']
rega = rega.astype('string')
list(df.shape)

drop_items = ['Артикул',
 'Фристайл3000',
 'Комплектующие',
 'материалы',
 'работы',
 'услуги',
 'МПА60-125-50',
 'ФК-5-1-12',
 'ТМ-110Т.00',
 'КРМ-2',
 'ЭП-1',
 'МРВД-G 2-A-400',
 'МПМРВД-G2-A',
 'СДУ-М',
 'МП-СДУ-G1/2-A',
 'НГА-360-G 1-А',
 'МПН-G1-А',
 'ИБП ИМПУЛЬС ФРИСТАЙЛ 11-3000',
 'МПН-G 1.1/4-А',
 'МПА 60-25-32',
 'КРМ-1',
 'СДА',
 'МРВД-G 1.1/4-A-300',
 'МПМРВД-G 1.1/4-A',
 'МПН-G1/2-А',
 'НГА-360-G1/2-А',
 'КР',
 'КО',
 'ЗИ',
 'МПА 60-150-50',
 'ПП-1',
 'МРВД-G 1/4-A-600',
 'МРВД-G 1/4-A-500',
 'НГА-360-G 2-А',
 'МПН-G 2-A',
 'УГП 30-12-12',
 'ЭП-2',
 'СДУ',
 'УГП 30-6-12',
 'Хладон 125',
 'МПА 53-100-32',
 'ЦОД3 3.1-']
df = df[~df['Артикул'].isin(drop_items)]
data = df.loc[~df['Номер КП'].isin([5033,5345])]
data['Количество'] = data['Количество'].astype('float64')
data['Цена для конечного пользователя, руб.'] = data['Цена для конечного пользователя, руб.'].astype('float64').fillna(0)
data['Стоимость для конечного пользователя, руб.'] = data['Стоимость для конечного пользователя, руб.'].astype('float64').fillna(0)
data['Проектная скидка'] = data['Проектная скидка'].astype('float64').fillna(0)
data['Цена с проектной скидкой,\n  руб.'] = data['Цена с проектной скидкой,\n  руб.'].astype('float64').fillna(0)
data['Стоимость с проектной скидкой,\n  руб.'] = data['Стоимость с проектной скидкой,\n  руб.'].astype('float64').fillna(0)
data['Цена для конечного пользователя, $'] = data['Цена для конечного пользователя, $'].astype('float64').fillna(0)
data['Стоимость для конечного пользователя, $'] = data['Стоимость для конечного пользователя, $'].astype('float64').fillna(0)
data['Цена с проектной скидкой, $'] = data['Цена с проектной скидкой, $'].astype('float64').replace('-',0).fillna(0)
data['Стоимость с проектной скидкой, $'] = data['Стоимость с проектной скидкой, $'].astype('float64').fillna(0)
data['Цена с проектной скидкой,\n  $'] = data['Цена с проектной скидкой,\n  $'].replace('???', 0).astype('float64').fillna(0)
data['Цена с проектной скидкой,\n  долл. США'] = data['Цена с проектной скидкой,\n  долл. США'].astype('float64').fillna(0)
data['Стоимость с проектной скидкой,\n  долл. США'] = data['Стоимость с проектной скидкой,\n  долл. США'].astype('float64').fillna(0)
data['Цена,\n  руб. '] = data['Цена,\n  руб. '].replace('нет в ассортименте', 0).astype('float64').fillna(0)
data['Цена EXW,\n  $'] = data['Цена EXW,\n  $'].replace('-', 0).astype('float64').fillna(0)
'Стоимость EXW,\n  $'
data['Стоимость EXW,\n  $'] = data['Стоимость EXW,\n  $'].replace('-', 0).astype('float64').fillna(0)

data['Дата выдачи КП'] = data['Дата выдачи КП'].astype('datetime64')
data.shape

final_data = pd.DataFrame()
final_data ['Дата выдачи КП'] = data['Дата выдачи КП']
final_data ['Номер КП'] = data['Номер КП']
final_data['Версия'] = data['Версия']
final_data ['Артикул'] = data['Артикул']
#final_data ['Наименование'] = data['Наименование']
final_data ['Количество'] = data['Количество']
# USD = 87; EUR = 95
final_data ['Цена_РРЦ'] = data[ 'Цена для конечного пользователя, руб.'].fillna(0) +data[ 'Цена для конечного заказчика'].fillna(0)*87 + data[ 'Цена для конечного пользователя, $'].fillna(0)*87 + data[ 'Цена для конечного пользователя,$'].fillna(0)*87 + data[ 'Цена,\n  руб. '].fillna(0) + data[ 'Цена для конечного пользователя, руб.- 1'].fillna(0) + data[ 'Цена для конечного пользователя, руб.- 2'].fillna(0)*87 + data[ 'Цена для конечного пользователя, руб'].fillna(0) + data[ 'Цена , руб.'].fillna(0) + data[ 'Цена для конечного пользователя, $.'].fillna(0)*87 + data[ 'Текущая цена для конечного пользователя, $'].fillna(0)*87 + data[ 'Текущая цена для конечного пользователя, руб.'].fillna(0) + data[ 'Цена для конечного пользователя, €'].fillna(0)*90 + data[ 'Цена для конечного пользователя'].fillna(0) + data[ 'Цена для конечного пользователя, Руб.'].fillna(0) + data[ 'Цена для конечного пользователя, USD.'].fillna(0)*87



final_data ['Сумма_РРЦ'] = data[ 'Стоимость для конечного пользователя, руб.'].fillna(0) + data[ 'Стоимость для конечного заказчика'].fillna(0)*87 + data[ 'Стоимость для конечного пользователя, $'].fillna(0)*87 + data[ 'Стоимость для конечного пользователя,$'].fillna(0)*87 + data[ 'Стоимость для конечного пользователя, руб'].fillna(0) + data[ 'Стоимость, руб.'].fillna(0)+data[ 'Стоимость для конечного пользователя, $.'].fillna(0)*87 + data[ 'Текущая стоимость для конечного пользователя, $'].fillna(0)*87 + data[ 'Текущая стоимость для конечного пользователя, руб.'].fillna(0) + data[ 'Стоимость для конечного пользователя, €'].fillna(0)*90 + data[ 'Стоимость для конечного пользователя'].fillna(0) + data[ 'Реальная Стоимость для конечного пользователя, руб.'].fillna(0) + data[ 'Стоимость руб.'].fillna(0) + data[ 'Стоимость , руб.'].fillna(0) + data[ 'Стоимость для конечного пользователя, Руб.'].fillna(0) + data[ 'Стоимость для конечного пользователя, USD.'].fillna(0)*87


final_data['Скидка'] = data[ 'Проектная скидка'].fillna(0) + data[ 'Стандартная скидка'].fillna(0) + data[ 'Скидка'].fillna(0) + data[ 'Скидка для конечного пользователя'].fillna(0) + data[ 'проектная скидка'].fillna(0) + data[ 'партнерская скидка'].fillna(0) + data[ 'Специальная скидка'].fillna(0) + data[ 'проектная  скидка'].fillna(0) + data[ 'Специальная скидка, %'].fillna(0) + data[ ' скидка ДЕМО'].fillna(0) + data[ 'Проектная скидка, %'].fillna(0) + data[ 'Проектная скидка технологического партнера'].fillna(0) + data[ 'РЕАЛЬНАЯ СКИДКА'].fillna(0) + data[ 'Дистрибьюторская скидка'].fillna(0) + data[ 'скидка'].fillna(0) + data[ 'от дистрибьютора скидка'].fillna(0) + data[ 'Реальная Проектная скидка ( в Дисттра)'].fillna(0) + data[ 'Проектная спец. скидка'].fillna(0)


final_data['Цена_скидка'] = data['Цена с проектной скидкой,\n  руб.'].fillna(0) + data[ 'Цена со стандартной скидкой,\n  руб.'].fillna(0) + data[ 'Цена с проектной скидкой'].fillna(0)*87 + data[ 'Цена для конечного пользователя со скидкой, руб.'].fillna(0) + data[ 'Цена с проектной скидкой, руб.'].fillna(0) + data[ 'Цена со стандартной скидкой, руб.'].fillna(0) + data[ 'Цена с проектной скидкой, $'].fillna(0)*87 + data[ 'Цена партнерская, руб.'].fillna(0) + data[ 'Цена со  скидкой,\n  руб.'].fillna(0) + data[ 'Цена с проектной скидкой,\n$'].fillna(0)*87 + data[ 'Цена с проектной скидкой,\nдолларов США.'].fillna(0)*87 + data[ 'Цена со специальной скидкой,\n  руб.'].fillna(0) + data[ 'Цена со специальной скидкой,\n  $'].fillna(0)*87 + data[ 'Цена со специальной скидкой, руб.'].fillna(0) + data[ 'Цена со специальной скидкой, '].fillna(0) * 87 + data[ 'Цена со специальной скидкой, $'].fillna(0)*87 + data[ 'Цена со специальной скидкой, руб'].fillna(0) + data[ 'Цена с проектной скидкой,\n  $'].fillna(0)*87 + data[ 'Стоимость со специальной  скидкой,\n  руб.'].fillna(0) + data[ 'Стоимость с проектной  скидкой,\n  руб.'].fillna(0) + data[ 'Цена со стандартной скидкой,\n  $'].fillna(0)*87 + data[ 'Цена с проектной скидкой,\n  долл. США'].fillna(0)*87 + data[ 'Цена с проектной скидкой,\n $'].fillna(0)*87 + data[ 'Цена с проектной скидкой, по условиям №2\n  руб.'].fillna(0) + data[ 'Цена с проектной скидкой по условиям №1,\n  руб.'].fillna(0) + data[ 'Цена с проектной скидкой,\n  руб. - 1'].fillna(0) + data[ 'Цена дистрибьютора, руб'].fillna(0) + data[ 'Цена с проектной скидкой, руб'].fillna(0) + data[ 'Цена с проектной скидкой, $.'].fillna(0)*87 + data[ 'Цена со стандартной скидкой, $.'].fillna(0)*87 + data[ 'Цена с проектной скидкой,\n  €'].fillna(0)*90 + data[ 'Цена с проектной скидкой, €'].fillna(0)*90+ data[ 'Цена с проектной скидкой,\nруб.'].fillna(0) + data[ 'Реальная Цена с проектной скидкой,\n  руб. ( в дистра)'].fillna(0) + data[ 'Цена со скидкой, руб.'].fillna(0) + data[ 'цена со скидкой'].fillna(0) + data[ 'Цена cо скидкой, руб.'].fillna(0) + data[ 'Цена с проектной скидкой,\n  Руб.'].fillna(0) + data[ 'Цена с проектной скидкой,\n  USD.'].fillna(0)*87 + data[ 'спец ЕНДЮЗЕР'].fillna(0) + data[ 'Цена со стандартной скидкой, руб'].fillna(0) + data[ 'Цена со скидкой от , руб.'].fillna(0) + data[ 'Цена с проектной скидкой,\n  $.'].fillna(0)*87



final_data['Сумма_скидка'] = data[ 'Стоимость с проектной скидкой,\n  руб.'].fillna(0) + data[ 'Стоимость со стандартной скидкой,\n  руб.'].fillna(0) + data[ 'Стоимость со проектной скидкой'].fillna(0)*87 + data[ 'Стоимость для конечного пользователя со скидкой, руб.'].fillna(0) + data[ 'Стоимость с проектной скидкой, руб.'].fillna(0) + data[ 'Стоимость со стандартной скидкой, руб.'].fillna(0) +data[ 'Стоимость с проектной скидкой, $'].fillna(0)*87 + data[ 'Стоимость партнерская, руб.'].fillna(0) + data[ 'Стоимость со  скидкой,\n  руб.'].fillna(0) + data[ 'Стоимость с проектной скидкой,\n$'].fillna(0)*87 + data[ 'Стоимость с проектной скидкой,\nдолларов США.'].fillna(0)*87 + data[ 'Стоимость со специальной скидкой,\n  руб.'].fillna(0) + data[ 'Стоимость со специальной скидкой,\n  $'].fillna(0)*87 + data[ 'Стоимость со специальной скидкой, руб.'].fillna(0) + data[ 'Стоимость со специальной скидкой, $'].fillna(0)*87 + data[ 'Стоимость со специальной скидкой, руб'].fillna(0) + data[ 'Стоимость с проектной скидкой,\n  $'].fillna(0)*87 + data[ 'Стоимость для конечного пользователя, руб..1'].fillna(0) + data[ 'Цена со стандартной скидкой,\n  $'].fillna(0)*87 + data[ 'Стоимость со стандартной скидкой,\n $'].fillna(0)*87 + data[ 'Стоимость с проектной скидкой,\n  долл. США'].fillna(0)*87 + data[ 'Стоимость с проектной скидкой,\n $'].fillna(0)*87 + data[ 'Стоимость с проектной скидкой,\n  руб..1'].fillna(0) + data[ 'Стоимость для дистрибьютора, руб'].fillna(0) + data[ 'Стоимость с проектной скидкой, руб'].fillna(0) + data[ 'Стоимость с проектной скидкой, $.'].fillna(0)*87 + data[ 'Стоимость со стандартной скидкой, $.'].fillna(0)*87 + data[ 'Стоимость с проектной скидкой,\n  €'].fillna(0)*90 + data[ 'Стоимость с проектной скидкой, €'].fillna(0)*90 + data[ 'Стоимость с проектной скидкой'].fillna(0) + data[ 'Стоимость с проектной скидкой,\nруб.'].fillna(0) + data[ 'Стоимость со скидкой, руб.'].fillna(0) + data[ 'стоимость со скидкой'].fillna(0) + data[ 'Стоимость с проектной скидкой,\n  Руб.'].fillna(0) + data[ 'Стоимость с проектной скидкой,\n  USD.'].fillna(0)*87 + data[ 'Стоимость со скидкой , руб.'].fillna(0) + data[ 'Стоимость со стандартной скидкой,  руб.'].fillna(0) + data[ 'Стоимость с проектной скидкой,\n  $.'].fillna(0)*87

final_data['Цена_РРЦ'] = final_data['Сумма_скидка'].round(0)
final_data['Сумма_РРЦ'] = final_data['Сумма_скидка'].round(0)
final_data['Скидка'] = final_data['Скидка'].round(2)
final_data['Цена_скидка'] = final_data['Сумма_скидка'].round(0)
final_data['Сумма_скидка'] = final_data['Сумма_скидка'].round(0)

final_data['Сумма_скидка'] = np.where((final_data['Сумма_скидка'] == 0) & (final_data['Сумма_РРЦ'] == 0) & (final_data['Количество'] != 0), final_data['Сумма_РРЦ'], final_data['Сумма_скидка'])
final_data

final_data.to_csv('final_data_2021.csv', sep = ';')
