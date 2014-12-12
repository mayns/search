# -*- coding: utf-8 -*-

__author__ = 'nyash myash'

import codecs

def do_list(path):
    f = codecs.open(path, encoding=u'utf-8')
    poems = []
    s = u''
    for line in f.readlines():
        if line != u'\n' and  u'* * *' not in line:
            s+= line
        else:
            if s:
                poems.append(s)
                s = ''
    else:
        if s:
            poems.append(s)
    return poems

poems = do_list(u'oster.txt')
#
for item in poems:
    print item


request = raw_input().decode(encoding='utf-8')

for item in poems:
    if request in item:
        print poems.index(item)+1




