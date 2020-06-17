# Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое программирование», «сокет», «декоратор». 
# Проверить кодировку файла по умолчанию. Принудительно открыть файл в формате Unicode и вывести его содержимое.
from chardet import detect

new_file = 'c:/Users/sav/Desktop/test_file.txt'

with open(new_file, 'w') as f_obj:
    f_obj.write('сетевое программирование\n сокет\n декоратор')
    print(f_obj)

with open(new_file, 'rb') as f_obj:
    content = f_obj.read()
    encoding = detect(content)['encoding']
    print(f'Кодировка файла по-умолчанию -> {encoding}.')


with open(new_file, 'r', encoding=encoding) as f_obj:
    for line in f_obj:
        print(line)