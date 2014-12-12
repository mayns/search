# -*- coding: utf-8 -*-

import operator
import random

def getwordfromindex(word):
  return [(random.randrange(100),random.randrange(100),'verb')]

def check_phrase(phrase):
  res_tuples = []
  for word in phrase:
    res_tuples.extend(getwordfromindex(word))
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

#TODO CHCK ALL BELOW
def process_request(request):
  #TODO change for oks method
  #search_phrases = oks.amazingfun(request)
  search_phrases = ['жопа']

  max_inclusion_len = 0
  pretendents = []

  for phrase in search_phrases:
    res = check_phrase(phrase)
    if max_inclusion_len == res[0]:
      pretendents.append(res[1])
    if max_inclusion_len < res[0]:
      pretendents = []
      pretendents.append(res[1])
      max_inslusion_len = res[0]

  #check pos score and get the winner phrase
  len_scores = {}
  for elem in pretendents:
    middiff = 0
    for d in elem:
      middiff += elem[d]
    middiff /= len(elem[1])
    len_scores.update({elem:middiff})
    
  #getmaxid
  max_id = 0
  max_val = 0
  for i in range(len(pretendents)):
    if max_val < len_scores[i]:
      max_id = i
      max_val = len_scores[i]

  #TODO sort by pos score
  return pretendents[max_id][1].keys()

while(True):
  print 'Hi there! I am ready to process your request...'
  res = process_request(raw_input())

#TODO we may OGREBSTY from the fact, that we may get several inclusions of a word inside one poem
