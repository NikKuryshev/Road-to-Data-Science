import os
import pandas as pd
import PySimpleGUI as sg
import menu

def find_file_by_number(directory, file_number):
    for root, dirs, files in os.walk(directory):
        for name in files:
            if file_number in name:
                return os.path.join(root, name)
    raise FileNotFoundError(f"Файл с номером {file_number} не найден в директории {directory}")


def choose_kp_file():
    # функция для выбора пути к файлу КП
    while True:
        kp_file_path_or_number = sg.popup_get_text('Введите номер файла КП или путь к файлу', title='Выбор файла КП')
        if os.path.exists(kp_file_path_or_number):
            return kp_file_path_or_number
        else:
            try:
                kp_file_path = find_file_by_number(r'C:\Users\nkuryshev\YandexDisk\C3 Presale', kp_file_path_or_number)
                return kp_file_path
            except FileNotFoundError:
                sg.popup('Файл не найден, попробуйте еще раз.', title='Ошибка')


if __name__ == '__main__':
    # Путь до директории с файлами Мастер файла
    master_file_dir = r'C:\Users\nkuryshev\Desktop'

    # Получаем путь до файла с основной информацией
    master_file_path = os.path.join(master_file_dir, 'Мастер_файл_v1.4.xlsx')

    # Читаем данные из файла с основной информацией
    master_price_df = pd.read_excel(master_file_path, sheet_name='Price', header = 0)
    master_price_ext_df = pd.read_excel(master_file_path, sheet_name='Price_ext', header = 0)

    # Выбор файла КП
    kp_file_path = choose_kp_file()

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

    sg.popup(f'Результат сохранен в файл: {result_file_path}', title='Успех')