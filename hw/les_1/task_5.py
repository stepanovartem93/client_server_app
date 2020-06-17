# Выполнить пинг веб-ресурсов yandex.ru, youtube.com и преобразовать результаты из байтовового в строковый тип на кириллице.
import subprocess
import chardet

print('*'*25 + 'youtube ping' + '*'*25)
source = ['ping', 'youtube.com']
subproc_ping = subprocess.Popen(source, stdout=subprocess.PIPE)
for line in subproc_ping.stdout:
    result = chardet.detect(line)
    data = line.decode(result['encoding']).encode('utf-8')
    print(data.decode('utf-8'))


# print('*'*25 + 'yandex ping' + '*'*25)
# source = ['ping', 'yandex.ru']
# subproc_ping = subprocess.Popen(source, stdout=subprocess.PIPE)
# for line in subproc_ping.stdout:
#     result = chardet.detect(line)
#     data = line.decode(result['encoding']).encode('utf-8')
#     print(data.decode('utf-8'))