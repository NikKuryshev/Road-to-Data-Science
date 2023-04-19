import tkinter as tk
import os

def find_file_by_number(directory, file_number):
    for root, dirs, files in os.walk(directory):
        for name in files:
            if file_number in name:
                return os.path.join(root, name)
    raise FileNotFoundError(f"Файл с номером {file_number} не найден в директории {directory}")

def choose_kp_file():
    # функция для выбора пути к файлу КП
    while True:
        kp_file_number = kp_file_number_entry.get()
        kp_file_path = find_file_by_number(r'C:\Users\nkuryshev\YandexDisk\C3 Presale', kp_file_number)
        if os.path.exists(kp_file_path):
            kp_file_path_var.set(kp_file_path)
            break
        else:
            kp_file_path_var.set('Файл не найден, попробуйте еще раз.')

# Создание главного окна
root = tk.Tk()
root.title('Меню выбора КП файла')

# Создание элементов интерфейса
kp_file_number_label = tk.Label(root, text='Номер КП файла:')
kp_file_number_entry = tk.Entry(root)
kp_file_path_label = tk.Label(root, text='Путь к выбранному КП файлу:')
kp_file_path_var = tk.StringVar()
kp_file_path_entry = tk.Entry(root, textvariable=kp_file_path_var, state='readonly')
choose_file_button = tk.Button(root, text='Выбрать файл', command=choose_kp_file)

# Размещение элементов интерфейса на главном окне
kp_file_number_label.pack()
kp_file_number_entry.pack()
kp_file_path_label.pack()
kp_file_path_entry.pack()
choose_file_button.pack()

# Запуск основного цикла обработки событий
root.mainloop()