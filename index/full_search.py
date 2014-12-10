# -*- coding: utf-8 -*-

__author__ = 'nyash myash'

import codecs
import re

delete = re.compile(r'\W+?|\d+?', re.UNICODE)
clr = re.compile(r'\s+', re.UNICODE)

def clear(s):
    """очищает строку и приводит к нижнему регистру"""
    s = delete.sub(' ', s)
    s = clr.sub(u' ', s).strip()
    return s.lower()

# сохраняем четверостишья в массив
f = codecs.open(u'poems.txt', encoding=u'utf-8')
poems = []
s = u''
for line in f.readlines():
    if line != u'\n':
        s+= line
    else:
        if s:
            poems.append(s)
            s = ''
else:
    if s:
        poems.append(s)


request = raw_input().decode(encoding='utf-8')
request = clear(request)


# полнотекстовый поиск
# мне кажется, от него стоит вообще отказаться, иначе на большом объеме стихов мы зависнем, так и не дойдя до поиска
# по индексу. вместо него лучше использовать вхождение нормальных форм этих слов с минимальным расстоянием
for item in poems:
    temp = clear(item)
    if u' ' not in request:
        if request in temp.split():
            print item
    else:
        if request in temp:
            print item
