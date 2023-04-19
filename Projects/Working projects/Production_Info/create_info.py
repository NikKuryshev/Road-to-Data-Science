import os
import pandas as pd
import numpy as np
import openpyxl
import xlsxwriter
import re

def find_file_by_number(directory_path, file_number):
    """
    Находит файл по указанному номеру в директории.
    Возвращает путь к файлу, если он найден, иначе возвращает None.
    """
    files = os.listdir(directory_path)
    for file in files:
        match = re.search(r'\d+', file)
        if match and int(match.group(0)) == file_number:
            return os.path.join(directory_path, file)
    return None


def choose_kp_file():
    # функция для выбора пути к файлу КП
    while True:
        kp_file_path = input('Введите путь до файла КП: ')
        if os.path.exists(kp_file_path):
            return kp_file_path
        else:
            print('Файл не найден, попробуйте еще раз.')


if __name__ == '__main__':
    # Путь до директории с файлами Мастер файла
    master_file_dir = r'C:\Users\nkuryshev\Desktop'

    # Получаем путь до файла с основной информацией
    master_file_path = os.path.join(master_file_dir, 'Мастер_файл_v1.4.xlsx')

    # Читаем данные из файла с основной информацией
    master_price_df = pd.read_excel(master_file_path, sheet_name='Price', header = 0)
    master_price_ext_df = pd.read_excel(master_file_path, sheet_name='Price_ext', header = 0)

    # Выбор файла КП
    kp_file_number = int(input('Введите номер файла КП: '))
    kp_file_dir = r'C:\Users\nkuryshev\YandexDisk\C3 Presale\=КП'
    kp_file_path = find_file_by_number(kp_file_dir, kp_file_number)

    if kp_file_path is None:
        print('Файл не найден, попробуйте еще раз.')
        exit()

    # Чтение данных из файла КП
    kp = pd.read_excel(kp_file_path, usecols=[2, 3, 4], header = 14)
    kp_df = kp.dropna(subset= ['Артикул'])

    # Объединение таблиц по артикулу
    merged_df = pd.merge(kp_df, master_price_df, on='Артикул', how='left')
    merged_df = pd.merge(merged_df, master_price_ext_df, on='Артикул', how='left', suffixes= ('_price','_price_ext'))

    # Выбор нужных столбцов
    k = merged_df.columns
    result_df = merged_df[['Артикул', 'Наименование_x', 'Количество', 'Входная цена, руб._price', 'Производитель_price',
                           'Оригинальный артикул', 'Входная цена, руб._price_ext','Производитель_price_ext','Оригинальный артикул/наименование','Примечание_price_ext']]

    # Сохранение результата в новый файл
    result_file_path = os.path.splitext(kp_file_path)[0] + '_информация для производства.xlsx'
    result_df.to_excel(result_file_path, index=False)

    print("Результат сохранен в файл:", result_file_path)