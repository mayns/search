# -*- coding: utf-8 -*-

from urllib import quote
import urllib2
import json

__author__ = 'mayns'

KEY = u'dict.1.1.20141207T200218Z.c01ef3f11cea86bf.3421773cbca3c8c8872988fc567a3815f27c0159'
YA_REQUEST = \
    lambda text, lang: u'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={key}&lang=' \
                             u'{lang}&text={text}&ui=ru'.format(key=KEY, lang=lang, text=quote(text.encode('utf-8')))


def get_syns(words, lang=u'ru-ru'):
    """
    :type words: list
    :param words: list of tuples from get_normal func
    rtype: list
    """
    syns_variants = []
    for word in words:
        word_syns = set()
        resp = urllib2.urlopen(YA_REQUEST(word[0], lang)).read()
        syns = json.loads(resp).get(u'def')
        if not syns:
            continue
        syns = syns[0].get(u'tr')
        if not syns:
            continue

        for syn in syns:
            if syn.get(u'pos') != word[1] or not syn.get(u'text'):
                continue
            word_syns.add(syn.get(u'text'))
            if syn.get(u'syn'):
                map(lambda x: word_syns.add(x['text']), syn['syn'])
        syns_variants.extend(list(word_syns))
    return syns_variants

d = {
    "head": {},
    "def": [
        {
            "text": "печаль",
            "pos": "существительное",
            "tr": [
                {
                    "text": "горесть",
                    "pos": "существительное",
                    "syn": [
                        {
                            "text": "скорбь",
                            "pos": "существительное"
                        },
                        {
                            "text": "огорчение",
                            "pos": "существительное"
                        }
                    ]
                },
                {
                    "text": "печалиться",
                    "pos": "глагол",
                    "syn": [
                        {
                            "text": "грустить",
                            "pos": "глагол"
                        },
                        {
                            "text": "скорбеть",
                            "pos": "глагол"
                        },
                        {
                            "text": "печалить",
                            "pos": "глагол"
                        },
                        {
                            "text": "опечалиться",
                            "pos": "глагол"
                        },
                        {
                            "text": "горевать",
                            "pos": "глагол"
                        },
                        {
                            "text": "опечалить",
                            "pos": "глагол"
                        },
                        {
                            "text": "огорчать",
                            "pos": "глагол"
                        },
                        {
                            "text": "огорчиться",
                            "pos": "глагол"
                        },
                        {
                            "text": "огорчить",
                            "pos": "глагол"
                        },
                        {
                            "text": "оплакивать",
                            "pos": "глагол"
                        }
                    ]
                },
                {
                    "text": "грусть",
                    "pos": "существительное"
                },
                {
                    "text": "горе",
                    "pos": "существительное",
                    "syn": [
                        {
                            "text": "горечь",
                            "pos": "существительное"
                        }
                    ]
                },
                {
                    "text": "горестный",
                    "pos": "прилагательное",
                    "syn":
                        [
                            {
                                "text": "печальный",
                                "pos": "прилагательное"
                            },
                            {
                                "text": "грустный",
                                "pos": "прилагательное"
                            },
                            {
                                "text": "скорбный",
                                "pos": "прилагательное"
                            },
                            {
                                "text": "тоскливый",
                                "pos": "прилагательное"
                            },
                            {
                                "text": "плачевный",
                                "pos": "прилагательное"
                            },
                            {
                                "text": "прискорбный",
                                "pos": "прилагательное"
                            }
                        ]
                },
                {
                    "text": "скорбящий",
                    "pos": "причастие"
                },
                {
                    "text": "тоска",
                    "pos": "существительное"
                },
                {
                    "text": "уныние",
                    "pos": "существительное",
                    "syn":
                        [
                            {
                                "text": "меланхолия",
                                "pos": "существительное"
                            }
                        ]
                },
                {
                    "text": "печально",
                    "pos": "наречие"
                },
                {
                    "text": "несчастье",
                    "pos": "существительное",
                    "syn":
                        [
                            {
                                "text": "беда",
                                "pos": "существительное"
                            }
                        ]
                },
                {
                    "text": "опечаленный",
                    "pos": "причастие"
                },
                {
                    "text": "траур",
                    "pos": "существительное",
                    "syn": [
                        {
                            "text": "плач",
                            "pos": "существительное"
                        }
                    ]
                },
                {
                    "text": "страдание",
                    "pos": "существительное"
                },
                {
                    "text": "тосковать",
                    "pos": "глагол"
                },
                {
                    "text": "сожаление",
                    "pos": "существительное"
                }
            ]
        }
    ]
}
