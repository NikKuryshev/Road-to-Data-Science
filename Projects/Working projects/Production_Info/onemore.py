import os
import menu

if __name__ == '__main__':
    directory = r'C:\Users\nkuryshev\YandexDisk\C3 Presale'
    file_number = input('Введите номер файла КП: ')
    file_path = menu.find_file_by_number(directory, file_number)

    menu.search_by_kp(file_path)