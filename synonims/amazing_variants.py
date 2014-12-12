# -*- coding: utf-8 -*-

from index.normal_form import get_normal
from synonims import get_syns
from itertools import *

__author__ = 'oks'


def amazing_fun(boring_string, lang=u'ru-ru'):

    variants = []
    raw = boring_string.split(u' ')
    original = [get_normal(w) for w in raw]

    for version in original:
        syns_block = get_syns(version, lang)
        variants.append(syns_block)
    columns = []
    flat_original = []
    for i in xrange(len(original)):
        flat_original.append(map(lambda x: x[0], original[i]))

    for i in xrange(len(original)):
        columns.append(flat_original[i])
        if variants[i]:
            columns[i].extend(variants[i])

    full_variants = product(*columns)
    amazing_variants = [' '.join(list(full_var)) for full_var in list(full_variants)]
    for var in amazing_variants:
        print var
    return amazing_variants

if __name__ == u'__main__':
    amazing_fun(u'выпить водочки да закусить огурчиком')