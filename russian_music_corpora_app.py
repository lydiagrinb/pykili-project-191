import os
import re
import pymorphy2

def search_lemma(lemma):
    lexema = pymorphy2.analyzer.Parse.lexeme
    result = []
    pattern_3 = 'муз.(.*)$'
    pattern_4 = 'слова(.*)$'
    pattern_5 = '(")\w.*\b(")'
    pattern_6 = '#(.*)$'
    pattern_7 = '\d\d\d\d'
    start_path = 'russian_music_corpora'
    for root, dirs, files in os.walk(start_path):
        for file in files:
            with open(file, encoding = 'utf-8'):
                text = file.read()
                a3 = re.search(pattern_3, text)
                a4 = re.search(pattern_4, text)
                a5 = re.search(pattern_5, text)
                a6 = re.search(pattern_6, text)
                a7 = re.search(pattern_7, text)
                if re.findall(lexema, text):
                    res1 = tuple(lexema, a3, a4, a5, a6, a7)
                    result.append(res1)
    return result

def search_token(token):
    result_found = []
    pattern_3 = 'муз.(.*)$'
    pattern_4 = 'слова(.*)$'
    pattern_5 = '(")\w.*\b(")'
    pattern_6 = '#(.*)$'
    pattern_7 = '\d\d\d\d'
    start_path = 'russian_music_corpora'
    for root, dirs, files in os.walk(start_path):
        for filename in files:
            with open(filename, encoding = 'utf-8'):
                text = file.read()
                print(text)
                a3 = re.search(pattern_3, text)
                a4 = re.search(pattern_4, text)
                a5 = re.search(pattern_5, text)
                a6 = re.search(pattern_6, text)
                a7 = re.search(pattern_7, text)
                if re.findall(token, text):
                    res2 = tuple(token, a3, a4, a5, a6, a7)
                    result_found.append(res2)
    return result_found

def search_a_song(song):
    songlist = []
    start_path = 'russian_music_corpora'
    for root, dirs, files in os.walk(start_path):
        for file in files:
            with open(file, encoding = 'utf-8'):
                text = file.read()
                if re.search(song, text):
                    songlist.append(text)
    return songlist

def search_with_name(name):
    list_name = []
    pattern = '\".*\"$'
    start_path = 'russian_music_corpora'
    for root, dirs, files in os.walk(start_path):
        for filename in files:
            with open(filename, encoding = 'utf-8'):
                text = filename.read()
            if re.findall(name, text):
                c = re.search(pattern, text)
                list_name.append(c)
    return list_name

start_work = int(input('найти слово - 1, найти и проанализировать песню - 2, запросить песню - 3'))

if start_work == 1:
    work_with_words = int(input('лемма - 1, словоформа - 2'))
    if work_with_words == 1:
        lemma = input('Введите искомое слово (в начальной форме:')
        print(search_lemma(lemma))
    elif work_with_words == 2:
        token = input('Введите слово в нужной форме:')
        print(search_token(token))

elif start_work == 2:
    song_search = int(input('поиск по названию - 1, по имени автора/исполнителя - 2'))
    if song_search == 1:
        song = input('Введите название песни:')
        print(search_a_song(song))
    elif song_search == 2:
        name = input('Введите автора или исполнителя песни:')
        na = search_with_name(name)
        print(na)

elif start_work == 3:
    request = input('Песня:')
    date = input('Дата запроса:')
    with open('song_requests.txt', 'a', encoding = 'utf-8')as f:
        f.write(request)
        f.write(' ')
        f.write(date)
        f.write('\n')
    print('Запрос принят!')
