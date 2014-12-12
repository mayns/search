# -*- coding: utf-8 -*-

__author__ = 'nyash myash'

import codecs
import operator
import random
import index.poems_index as index
import codecs
import json
from synonims.amazing_variants import amazing_fun
import yobi

def do_list(path):
    f = codecs.open(path, encoding=u'utf-8')
    poems = []
    s = u''
    for line in f.readlines():
        if (line != u'\n') and  (u'*' not in line):
            s+= line
        else:
            if s:
                poems.append(s)
                s = ''
    else:
        if s:
            poems.append(s)
    return poems


#for item in poems:
#    print item


#for item in poems:
#    if request in item:
#        print poems.index(item)+1
poems = do_list(u'oster.txt')
#for item in poems:
#    print item
print len(poems)
#poems_index = index.do_index(poems)
with codecs.open('index.txt', 'r', encoding='utf-8') as f:
    r = f.read()
    poems_index = json.loads(r)
while(True):
  print 'Hi there! I am ready to process your request...'
  #print raw_input().decode(encoding='utf-8')
  res = yobi.process_request(raw_input().decode(encoding='utf-8'))
  if not res:
    print 'no res for req'
    continue

  

  for elem in res:
    print '* * *'
    print poems[elem]
    print 

#TODO we may OGREBSTY from the fact, that we may get several inclusions of a word inside one poem
