"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт, осуществляющий выборку определенных данных
из файлов info_1.txt, info_2.txt, info_3.txt и формирующий новый «отчетный» файл в формате CSV.
Для этого:
 - Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с данными, их открытие и
 считывание данных. В этой функции из считанных данных необходимо с помощью регулярных выражений извлечь
 значения параметров «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
 - Значения каждого параметра поместить в соответствующий список. Должно получиться четыре списка —
 например, os_prod_list, os_name_list, os_code_list, os_type_list.
 - В этой же функции создать главный список для хранения данных отчета — например, main_data — и поместить в него
 названия столбцов отчета в виде списка: «Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
 - Значения для этих столбцов также оформить в виде списка и поместить в файл main_data (также для каждого файла).
 - Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой функции реализовать получение
 данных через вызов функции get_data(), а также сохранение подготовленных данных в соответствующий CSV-файл.
"""
import re, csv

os_prod_list, os_name_list, os_code_list, os_type_list, main_data = [], [], [], [], []

def get_data():
    for i in range(1, 4):
        file_obj = open(f'info_{i}.txt')
        data = file_obj.read()

        # изготовитель системы
        pattern = re.compile(r'Изготовитель системы:\s*\S*')
        os_prod_list.append(pattern.findall(data)[0].split()[2])

        # название ОС
        pattern = re.compile(r'Название ОС:\s*\S*\s*\S*')
        os_name_list.append(pattern.findall(data)[0].split()[3])

        # Код продукта
        pattern = re.compile(r'Код продукта:\s*\S*')
        os_code_list.append(pattern.findall(data)[0].split()[2])

        # Тип системы
        pattern = re.compile(r'Тип системы:\s*\S*')
        os_type_list.append(pattern.findall(data)[0].split()[2])

    headers = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data.append(headers)

    data_values = [[os_prod_list], [os_name_list], [os_code_list], [os_type_list]]
    main_data.append(data_values)

print(main_data)
# print(os_prod_list, os_name_list, os_code_list, os_type_list)