import os
import re
import pymorphy2

def search_lemma(lemma):
    'lexema = pymorphy2.analyzer.Parse.lexeme'
    'word = lemma'
    'morph = pymorphy2.MorphAnalyzer.parse(word)'
    'lexema = morph.lexeme'
    'print(lexema)'
    result = []
    pattern_3 = 'муз. ([А-Я][а-я].*) ([А-Я][а-я].*)'
    pattern_4 = 'слова ([А-Я][а-я].*) ([А-Я][а-я].*)'
    pattern_5 = '(")(([А-Я][а-я].*).*)(")'
    pattern_6 = '#([а-я].*)((([а-я].*)|([А-Я][а-я].*)).*)'
    pattern_7 = '\d\d\d\d'
    start_path = 'C:/Users/Лидия/Desktop/russian_music_corpora'
    for root, dirs, files in os.walk(start_path):
        for filename in files:
            with open(filename, encoding = 'utf-8') as f:
                text = f.read()
                text1 = text.split()
                string = str(text1)
                string1 = string.lower()
                text2 = str(string1)
                string2 = re.sub('[.!?()"":;-'']', '', text2)
                stri = string2.split(', ')
                lemmas = []
                for word in stri:
                    print(word1)
                    p = pymorphy2.MorphAnalyzer.parse(word)
                    normal_form = p.normal_form
                    print(normal_form)
                    lemmas.append(normal_form)
                print(lemmas)
                a3 = re.search(pattern_3, text)
                if a3:
                    b3 = a3.group()
                else:
                    b3 = None
                a4 = re.search(pattern_4, text)
                if a4:
                    b4 = a4.group()
                else:
                    b4 = None    
                a5 = re.search(pattern_5, text)
                if a5:
                    b5 = a5.group()
                else:
                    b5 = None
                a6 = re.search(pattern_6, text)
                if a6:
                    b6 = a6.group()
                else:
                    b6 = None
                a7 = re.search(pattern_7, text)
                if a7:
                    b7 = a7.group()
                else:
                    b7 = None
                if lemma in lemmas:
                    res1 = (lemma, b3, b4, b5, b6, b7)
                    result.append(res2)
                    print(result)
    return result

def search_token(token):
    result_found = []
    pattern_3 = 'муз. ([А-Я][а-я].*) ([А-Я][а-я].*)'
    pattern_4 = 'слова ([А-Я][а-я].*) ([А-Я][а-я].*)'
    pattern_5 = '(")(([А-Я][а-я].*).*)(")'
    pattern_6 = '#([а-я].*)((([а-я].*)|([А-Я][а-я].*)).*)'
    pattern_7 = '\d\d\d\d'
    start_path = 'C:/Users/Лидия/Desktop/russian_music_corpora'
    for root, dirs, files in os.walk(start_path):
        for filename in files:
            with open(filename, encoding = 'utf-8') as f:
                text = f.read()
                a3 = re.search(pattern_3, text)
                if a3:
                    b3 = a3.group()
                else:
                    b3 = None
                a4 = re.search(pattern_4, text)
                if a4:
                    b4 = a4.group()
                else:
                    b4 = None    
                a5 = re.search(pattern_5, text)
                if a5:
                    b5 = a5.group()
                else:
                    b5 = None
                a6 = re.search(pattern_6, text)
                if a6:
                    b6 = a6.group()
                else:
                    b6 = None
                a7 = re.search(pattern_7, text)
                if a7:
                    b7 = a7.group()
                else:
                    b7 = None
                if re.findall(token, text):
                    res2 = (token, b3, b4, b5, b6, b7)
                    result_found.append(res2)
                    print(result_found)
    return result_found

def search_a_song(song):
    songlist = []
    start_path = 'C:/Users/Лидия/Desktop/russian_music_corpora'
    for root, dirs, files in os.walk(start_path):
        for filename in files:
            with open(filename, encoding = 'utf-8') as f:
                text = f.read()
            if song in text:
                songlist.append(text)
                print(text)
    return songlist

def search_with_name(name):
    list_name = []
    pattern = '\".*\"$'
    start_path = 'C:/Users/Лидия/Desktop/russian_music_corpora'
    for root, dirs, files in os.walk(start_path):
        print('Files на этом уровне:', files)
        for filename in files:
            with open(filename, encoding = 'utf-8') as f:
                text = f.read()
            if re.findall(name, text):
                c = re.search(pattern, text)
                list_name.append(c)
                print(text)
    return list_name

start_work = int(input('найти слово - 1 \nнайти и проанализировать песню - 2 \nзапросить песню - 3 \n'))

if start_work == 1:
    work_with_words = int(input('лемма - 1, словоформа - 2\n'))
    if work_with_words == 1:
        lemma = input('Введите искомое слово (в начальной форме):')
        search_lemma(lemma)
    elif work_with_words == 2:
        token = input('Введите слово в нужной форме:')
        search_token(token)

elif start_work == 2:
    song_search = int(input('поиск по названию - 1 \nпо имени автора/исполнителя - 2 \n'))
    if song_search == 1:
        song = input('Введите название песни:')
        search_a_song(song)
    elif song_search == 2:
        name = input('Введите автора или исполнителя песни:')
        search_with_name(name)
        
elif start_work == 3:
    request = input('Песня:')
    date = input('Дата запроса:')
    with open('song_requests.txt', 'a', encoding = 'utf-8')as f:
        f.write(request)
        f.write(' ')
        f.write(date)
        f.write('\n')
    print('Запрос принят!')
