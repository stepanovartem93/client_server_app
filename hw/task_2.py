# Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов 
# (не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.

words = [b'class', b'function', b'method']

for word in words:
    print(f'The type of word {word} is {type(word)} and length - {len(word)}.')