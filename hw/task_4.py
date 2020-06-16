# Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое и 
# выполнить обратное преобразование (используя методы encode и decode).

words = ['разработка', 'администрирование', 'protocol', 'standard']

for word in words:
    to_encode = word.encode('utf-8')
    print(f'Слово "{word}" в байтовом представлении -> {to_encode}')
    to_decode = to_encode.decode('utf-8')
    print(f'Слово "{word}" в строковомы представлении -> {to_decode}')
    print('-'*50)