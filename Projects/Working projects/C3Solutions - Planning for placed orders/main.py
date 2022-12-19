import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', None)

# типа константы
path1 = "C:\\Users\\nkuryshev\\Desktop\\Offer C3 Solutions 5486 AT-Consulting 07.12.2022 v2 (2).xlsx"
path2 = "C:\\Users\\nkuryshev\\Desktop\\Offer C3 Solutions 5612 Softline 14.12.2022.xlsx"
path3 = "C:\\Users\\nkuryshev\\Desktop\\Offer C3 Solutions 4087 ICL 13.12.2022 v8.xlsx"
path4 = "C:\\Users\\nkuryshev\\Desktop\\Offer C3 Solutions 4679 Telecom Integratsiya 28.07.2022 v3 (1).xlsx"
paths = [path4]
#удаление услуг из базы данных
drop_item = ['C3.DI9999', 'C3.DI9998', 'C3.DL0000', 'C3.DL0001', 'C3.DL0002', 'C3.DL0003', 'C3.DL0004', \
	'C3.DL0005', 'C3.DL0006', 'C3.AD9999', 'C3.TP9999', 'C3.MM9999', 'C3.SP9999', 'C3.CX9999', 'C3.IX9999', 'C3.UP9999', \
	'C3.WARRANTY2Y', 'C3.WARRANTY3Y', 'C3.WARRANTY4Y', 'C3.WARRANTY5Y']
#функции по которым идет объединение столбцов
aggregation = {'Наименование':'first', 'Количество':'sum', 'Единица измерения':'first','Цена для конечного пользователя, руб.':'sum',
               'Стоимость для конечного пользователя, руб.':'sum', 'Проектная скидка':'mean', 'Цена с проектной скидкой,\n  руб.':'sum', 'Стоимость с проектной скидкой,\n  руб.':'sum'}

# Чтение эксель файла по заданному пути, начиная с 15 строки, используя только заданные столбцы
#def openoffer (path):
    #wb = openpyxl.load_workbook(path, read_only=True)
    #offers = ['offer_машзал1', 'offer_машзал2', 'offer_машзал3', 'offer_кроссовая', 'запрос']
    #for sheet in wb:
    #    offers.append(sheet.title)
    #for offer in offers:
   #     dict = pd.read_excel(path, sheet_name=offers, skiprows = 14, usecols = 'C:K')
  #  for key,arg in dict:
 #       df = pd.concat(arg).reset_index(drop=True)
    #df = df.dropna().loc[~df['Артикул'].isin(drop_item)]
 #   return dict


#df = pd.DataFrame()
#for path in paths:
  #  df = pd.concat([df, openoffer(path)])

#print(df)

"""#Проверка открытия двух файлов и объединения в общаю базу данных
it = openoffer(path1)
newdata = readdata(it)
it = openoffer(path2)
newdata = pd.concat([newdata, readdata(it)])
print(newdata.groupby('Артикул').agg(aggregation))
newdata.set_index('Артикул', inplace = True)
#Балуемся с графиками
newdata['Количество'].plot(kind = 'barh')
plt.show()"""