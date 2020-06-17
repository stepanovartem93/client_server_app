# Определить, какие из слов «attribute», «класс», «функция», «type» невозможно записать в байтовом типе.

words = [b'attribute', b'класс', b'функция', b'type']

for word in words:
    print(word)


#выскакивает ошибка SyntaxError, с указанием на букву -> b <- рядом с словом класс, значит русские слова невозможно записать в байтовом типе


# почему не срабатывает обработка ошибок try - except?
# for word in words:
#     try:
#         print(word)
#     except SyntaxError:
#         print(f'Слово - {word} невозможно записать в байтовом типе')