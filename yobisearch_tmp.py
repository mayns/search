import operator

def check_phrase(self, phrase):
  res_tuples = []
  for word in phrase:
    res_tuples.append(elem for elem in getwordfromindex(word))
  res_dict = {}
  #iterate through all tuples from index and build a dict
  #dict = {id of word in index : list of all tuples from index info}
  for elem in res_tuples:
    if elem[0] in res_dict.keys:  
      res_dict.update({elem[0]: dict.get(elem[0]).append(elem)})
    else:
      res_dict.add((elem))
  
  maxlen = max(res_dict.iteritems(), lambda values: len(values))

  res = []
  for elem_id in res_dict.values():
    if(len(res_dict[elem_id])) == maxlen:
      res.append({elem_id:res_dict[elem_id]})

  score_table = {}
  for elem_id in res:
    values = res[elem_id]
    if maxlen == 1:
      score_table.update({elem_id,1})#1 for position scoring
    else:
      sor = sorted(values,key=lambda x: x[1])
      diff = (sor[len(sor)-1] - sor[0])/maxlen
      score_table.update({elem_id,diff})

  return(maxlen,score_table)

request = raw_input()
search_phrases = oksfuncreturningsynonims(request)

max_inclusion_len = 0
pretendents = []

for phrase in search_variants:
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

winner = [pretendents[max_id][1].keys()]

    
