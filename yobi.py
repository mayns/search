# -*- coding: utf-8 -*-

import operator
import random
import index.poems_index as index
import codecs
import json
from synonims.amazing_variants import amazing_fun

class NoResultException(Exception):
  def __init__(self, msg):
    super(NoResultException, self).__init__(msg)

def getwordfromindex(word):
  return poems_index[word]

def check_phrase(phrase):
  res_tuples = []
  for word in phrase:
    try:
      res_tuples.extend(getwordfromindex(word))
    except Exception:
      pass
	
  res_dict = {}
  #iterate through all tuples from index and build a dict
  #dict = {id of word in index : list of all tuples from index info}
  #tuple has the following struct: (id of a poem, pos of word in a poem, )
  for elem in res_tuples:
    if elem[0] in res_dict.keys():
      curr_val = res_dict[elem[0]]
      #WTF!!!! Can't append to dic[elem[0]]????
      curr_val.append(elem)
      res_dict[elem[0]] = curr_val 
    else:
      res_dict.update({elem[0]:[elem]})

  if not res_dict:
    return None
 
  #best result of inclusions 
  maxlen = max([len(res_dict[elem]) for elem in res_dict])
  res = {el_id:res_dict[el_id] for el_id in res_dict if len(res_dict[el_id]) == maxlen}
  score_table = {}
  for elem_id in res:
    values = res[elem_id]

    if maxlen == 1:
      score_table.update({elem_id:1})#1 for position scoring
    else:
      #TODO may cause problems if we have two identical tuples in res
      sor = sorted(values,key=lambda x: x[1])
      diff = (sor[len(sor)-1][1] - sor[0][1])/maxlen
      score_table.update({elem_id:diff})
  return(maxlen,score_table)

def process_request(request):
  #TODO change for oks method
  search_phrases = amazing_fun(request)
  print search_phrases
  max_inclusion_len = 0
  pretendents = []

  #remove all phrases scoring lower than max_len
  for phrase in search_phrases:
    res = check_phrase(phrase.split())
    if not res:
      continue
    if max_inclusion_len == res[0]:
      pretendents.append(res[1])
    if max_inclusion_len < res[0]:
      pretendents = []
      pretendents.append(res[1])
      max_inslusion_len = res[0]
  #check pos score and get the winner phrase
  #TODO potential bug when we will sort the list
  len_scores = []
  for elem in pretendents:
    middiff=0
    for d in elem:
      middiff += elem[d]
    middiff /= len(elem.keys())
    len_scores.append(middiff)

  if not len_scores:
    return None
 
  max_id = len_scores.index(max(len_scores))
  #TODO sort by pos score
  unsorted_res = list(pretendents[max_id])
  return sorted(unsorted_res,reverse=True)

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


poems = do_list(u'oster.txt')
#poems_index = index.do_index(poems)
with codecs.open('index.txt', 'r', encoding='utf-8') as f:
    r = f.read()
    poems_index = json.loads(r)
#for key in sorted(poems_index.keys()):
#  print key , poems_index[key]
for i in range(50):
  print
while(True):
  print 'Hi there! I am ready to process your request...'
  #print raw_input().decode(encoding='utf-8')
  res = process_request(raw_input().decode(encoding='utf-8'))
  if not res:
    print 'No result for your request'
    continue


  for elem in res:
    print '* * * ' +str(elem) + ' * * *'
    print poems[elem]
    print

#TODO пропала мама соврать
