# -*- coding: utf-8 -*-

__author__ = 'nyash myash'

import codecs
from normal_form import get_normal
import re



def do_index(l):
    """создает индекс. на вход - лист строк, каждая строка - отдельное четверостишье"""
    # delete = re.compile(u'\W+?|\d+?', re.UNICODE)
    poem_index = {}
    for i in xrange(len(l)):
        print 'creating index for poem ...', i
        pos = 0
        # sen = delete.sub(' ', l[i])
        # sen = sen.split()
        sen = l[i].split()
        # for s in sen:
        #     print s
        for word in sen:
            normal = get_normal(word)
            for item in normal:
                p_speech = item[1]
                if p_speech not in (u'PREP', u'CONJ', u'PRCL', u'INTJ'):
                    poem_index.setdefault(item[0],[]).append((i,pos,p_speech))
            pos +=1
    return poem_index

delete = re.compile(r'\W+?|\d+?', re.UNICODE)
pattern = re.compile(r'\s+', re.UNICODE)
# сохраняем четверостишья в массив
f = codecs.open(u'poems.txt', encoding=u'utf-8')
poems = []
s = u''
for line in f.readlines():
    if line != u'\n':
        s+= line
    else:
        if s:
            s = delete.sub(' ', s)
            s = re.sub(pattern, u' ', s).strip()
            poems.append(s.lower())
            s = ''
else:
    if s:
        s = delete.sub(u' ', s)
        s = re.sub(pattern, u' ', s).strip()
        poems.append(s.lower())

for item in poems:
    print item

# p_index = do_index(poems)
#
# for key in sorted(p_index.keys()):
#     print u'{0:14} ==> {1}'.format(key, p_index[key])



