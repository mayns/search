# -*- coding: utf-8 -*-

__author__ = 'nyash myash'


import pymorphy2

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
            p_speech.append(item.tag.POS)
    return zip(normal,p_speech)

if __name__ == '__main__':
    print get_normal(u'стали')
