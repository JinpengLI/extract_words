# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 20:41:11 2014

@author: Jinpeng Li
"""


class KeyWordsPage(object):
    def __init__(self, page_source, key_words):
        self.page_source = page_source
        self.key_words = key_words


class AroundContent(object):
    def __init__(self, left, right):
        self.left = left
        self.right = right

