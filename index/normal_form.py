# -*- coding: utf-8 -*-

__author__ = 'nyash myash'


import pymorphy2

pos_match = {
    u'NOUN': u'существительное',
    u'ADJF': u'прилагательное',
    u'ADJS': u'прилагательное',
    u'COMP': u'наречие',
    u'VERB': u'глагол',
    u'INFN': u'глагол',
    u'PRTF': u'причастие',
    u'PRTS': u'причастие',
    u'GRND': u'деепричастие',
    u'NUMR': u'числительное',
    u'ADVB': u'наречие',
    u'NPRO': u'местоимение',
    u'PRED': u'наречие'
}

def get_normal(word):
    """возвращает список туплей, содержащих нормальную форму и часть речи"""
    morph = pymorphy2.MorphAnalyzer()
    forms = morph.parse(word)
    normal = []
    p_speech = []
    for item in forms:
        p = item.normal_form
        if p not in normal:
            normal.append(p)
            p_speech.append(pos_match[item.tag.POS])
    return zip(normal, p_speech)

if __name__ == '__main__':
    print get_normal(u'стали')
