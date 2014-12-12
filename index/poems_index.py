# # -*- coding: utf-8 -*-
#
# __author__ = 'nyash myash'
#
import codecs
from normal_form import get_normal
import re
import json

delete = re.compile(u'[^а-яА-Я\-]+?', re.UNICODE)
clr = re.compile(r'\s+', re.UNICODE)

def do_list(path):
    f = codecs.open(path, encoding=u'utf-8')
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
    return poems



def do_index(l):
    """создает индекс. на вход - лист строк, каждая строка - отдельное четверостишье.
    возвращает словарь {normal_form : [(poem number, position in poem, part of speech)]}"""
    poem_index = {}

    for i in xrange(len(l)):
        print 'creating index for poem ...', i
        pos = 0
        sen = clear(l[i]).split()
        for word in sen:
            if u'ё' in word:
                word = word.replace(u'ё', u'е')
            if word == u'-':
                continue
            normal = get_normal(word)
            for item in normal:
                p_speech = item[1]
                if p_speech not in (u'предлог', u'союз', u'междометие', u'частицв'):
                    poem_index.setdefault(item[0], []).append((i, pos, p_speech))
            pos +=1
    return poem_index

def clear(s):
    """очищает строку и приводит к нижнему регистру"""
    s = delete.sub(' ', s)
    s = clr.sub(u' ', s).strip()
    return s.lower()


# poems = do_list(u'poems.txt')
#
# for item in poems:
#     print item
#
# p_index = do_index(poems)
#
# cur_index = json.dumps(p_index)
# with codecs.open('index.txt', 'w', encoding='utf-8') as f:
#     f.write(cur_index)
#
#
# with codecs.open('index.txt', 'r', encoding='utf-8') as f:
#     r = f.read()
#     restored_index = json.loads(r)
#
#
# for key in sorted(restored_index.keys()):
#     print u'{0:14} ==> {1}'.format(key, restored_index[key])



