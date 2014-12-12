# -*- coding: utf-8 -*-

from index.normal_form import get_normal
from synonims import get_syns
from itertools import *

__author__ = 'oks'


def amazing_fun(boring_string, lang=u'ru-ru'):

    variants = []
    raw = boring_string.split(u' ')
    normal_versions = [get_normal(w) for w in raw]
    print normal_versions
    for version in normal_versions:
        syns_block = get_syns(version, lang)
        variants.append(syns_block)
    columns = []
    for i in xrange(len(normal_versions)):
        columns.append(list(normal_versions[i][0]))
        if variants[i]:
            print columns[i]
            columns[i].extend(variants[i])
    full_variants = product(columns)
    for f in full_variants:
        print f
    # print [' '.join(list(full_var)) for full_var in list(full_variants)]

if __name__ == u'__main__':
    amazing_fun(u'город засыпает')