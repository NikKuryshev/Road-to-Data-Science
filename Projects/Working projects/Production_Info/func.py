import pandas as pd
import openpyxl
import numpy as np
import os

import re
import unicodedata


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
                        if file.startswith('Offer') and file.endswith(('xls', '.xlsx','.xlsm','.xltx','.xltm')):
                            actual_path = os.path.join(root, dir, file)
                            list_of_paths.append(actual_path)