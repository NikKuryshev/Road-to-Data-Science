import pandas as pd
import openpyxl
import os
import const
import re
import unicodedata


drop_item = ['C3.DI9999', 'C3.DI9998', 'C3.DL0000', 'C3.DL0001', 'C3.DL0002', 'C3.DL0003', 'C3.DL0004', \
	'C3.DL0005', 'C3.DL0006', 'C3.AD9999', 'C3.TP9999', 'C3.MM9999', 'C3.SP9999', 'C3.CX9999', 'C3.IX9999', 'C3.UP9999', \
	'C3.WARRANTY2Y', 'C3.WARRANTY3Y', 'C3.WARRANTY4Y', 'C3.WARRANTY5Y']
# тестовые данные
offers = ['offer_машзал1', 'offer_машзал2', 'offer_машзал3', 'offer_кроссовая', 'запрос']
path4 = "C:\\Users\\nkuryshev\\Desktop\\Offer C3 Solutions 4679 Telecom Integratsiya 28.07.2022 v3 (1).xlsx"

def read_path(path):

    """
    Функция по чтению пути до рабочего файла и папки из файла path
    :param path: Путь указанный пользователем в файле path.txt
    :return: root_kp: Путь до директории с КП
    """
    with open(path, encoding = 'UTF-8') as file:
        root_kp = str(file.readlines() [3])[:-1]    #папка с КП
    return root_kp
root_kp = read_path("path.txt") # Получение папки, где лежат все КП

def get_actual_kp_file(kp_numbers):
    """
    Получение пути до файла с КП по заданному номеру.
    :param kp_numbers: список номеров запрашиваемых КП
    :return list of paths: Список путей до файлов с КП
    """
    actual_path = ''
    list_of_paths = []
    # Определяем шаблон для поиска файла
    for kp_number in kp_numbers:
        for root, dirs, files in os.walk(root_kp):
            for dir in dirs:
                # Находим папку с номером КП
                if dir == str(kp_number):
                    files_on_dir = os.listdir(os.path.abspath(os.path.join(root, dir)))
                    for file in files_on_dir:
                        if file.startswith('Offer'):
                            actual_path = os.path.join(root, dir, file)
                            list_of_paths.append(actual_path)
    return list_of_paths
def get_sheet(path):

    """
    Чтение файла КП по заданному пути.
    Получение списка страниц файла.

    :param path: Путь к файлу
    :return: offer: Список страниц файла с офферами (Страница должна начинаться с 'offer_'
    """

    wb = openpyxl.load_workbook(path, read_only=True)
    offer = []
    for sheet in wb:
        if 'offer' in sheet.title:
            offer.append(sheet.title)
    return offer
    wb.close()
def get_offer_info(path):
    offer = openpyxl.load_workbook(path, data_only= True).active
    partner = unicodedata.normalize('NFKD',offer['C10'].value.replace('Партнер:  ', ''))
    customer = unicodedata.normalize('NFKD', offer['C11'].value.replace('Заказчик:  ', ''))
    distr = offer['C13'].value
    if distr != None:
        distr = unicodedata.normalize('NFKD', distr.replace('Дистрибьютор: ', ''))
    return partner, customer, distr
    offer.close()
def get_data(path, sheets):

    """
    Чтение файла КП по заданному пути, списку страниц файла.
    Получение базы данных с артикулами по всем страницам файла.
    :param path: Путь к файлу
    :param sheets: Список страниц файла КП
    :return: data: База данных по найденному файлу
    """

    data = pd.DataFrame()
    for sheet in sheets:
        dict = pd.read_excel(path, sheet_name=sheet, skiprows=14, usecols='C:K') # Чтение КП по заданным столбцам, начиная с 14 строки
        df = dict.dropna().loc[~dict['Артикул'].isin(drop_item)] # Удаление сервисных артикулов
        data = pd.concat([data,df]).reset_index(drop=True) # Объединение в общую базу данных, если есть несколько страниц в КП
        data['Дата выдачи КП'] = re.findall(r'\d{2}\.\d{2}\.\d{4}', path)[0]  # Добавление столбца с датой
        data['Номер КП'] = re.findall(r'\d{3,4}', path)[0]  # Добавление столбца с номером КП
    return data
def create_file(data):
    """
    Создать excel файл с базой данных
    :param data:  База данных
    :return:
    """
    data.sort_values('Количество', ascending=False).to_excel('./summary.xlsx', sheet_name='summary', index=False)

def category_data(data):
    """
    Создание базы данных с разделением артикулов на категории (шкафы, БРП итд) и подгруппы (C3.RF, C3.BS итд)
    :param data: база данных
    :return:
    """
    for key,value in const.categories.items():
        for arg in value:
            if arg in data['Артикул']:
                data['Категория'] = arg
    return data

