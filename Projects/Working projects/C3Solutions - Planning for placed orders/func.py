import pandas as pd
import openpyxl

drop_item = ['C3.DI9999', 'C3.DI9998', 'C3.DL0000', 'C3.DL0001', 'C3.DL0002', 'C3.DL0003', 'C3.DL0004', \
	'C3.DL0005', 'C3.DL0006', 'C3.AD9999', 'C3.TP9999', 'C3.MM9999', 'C3.SP9999', 'C3.CX9999', 'C3.IX9999', 'C3.UP9999', \
	'C3.WARRANTY2Y', 'C3.WARRANTY3Y', 'C3.WARRANTY4Y', 'C3.WARRANTY5Y']



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

def get_data(path, sheets):
    """
    Чтение файла КП по заданному пути, списку страниц файла.
    Получение базы данных с артикулами по всем страницам файла.
    :param path: Путь к файлу
    :param sheets:
    :return:
    """
    data = pd.DataFrame()
    for sheet in sheets:
        dict = pd.read_excel(path, sheet_name=sheet, skiprows=14, usecols='C:K')
        df = dict.dropna().loc[~dict['Артикул'].isin(drop_item)]
        data = pd.concat([data,df]).reset_index(drop=True)
    return data
offers = ['offer_машзал1', 'offer_машзал2', 'offer_машзал3', 'offer_кроссовая', 'запрос']
path4 = "C:\\Users\\nkuryshev\\Desktop\\Offer C3 Solutions 4679 Telecom Integratsiya 28.07.2022 v3 (1).xlsx"

of = get_sheet(path4)
get_data(path4, of)