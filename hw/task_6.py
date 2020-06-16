# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор». 
# Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.

new_file = 'c:/Users/sav/Desktop/test_file.txt'

# with open(new_file, 'w') as f_obj:
#     f_obj.write('сетевое программирование\n сокет\n декоратор')
#     print(f_obj)

# кодировка файла по умолчанию - win1251


with open(new_file) as f_obj:
    for line in f_obj:
        print(line)