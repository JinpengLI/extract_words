# -*- coding: utf-8 -*-
"""
Created on Thu Apr 17 20:48:07 2014

@author: Jinpeng Li
"""

import re
from extract_words.page import AroundContent


def get_around_one_keyword_pattern(one_page_source,
                                   key_word,
                                   left_min_around_len,
                                   right_min_around_len):
    """
    Example
    -------
    one_page_source = "1111ddd2222edde3333"
    min_around_len = 2
    left_min_around_len = right_min_around_len = min_around_len
    key_word = "dd"
    ret = get_around_one_keyword_pattern(one_page_source,
                                         key_word,
                                         left_min_around_len,
                                         right_min_around_len)
    """
    around_contents = []
    pattern = "(.{%d})%s(.{%d})" % (left_min_around_len,
                                    re.escape(key_word),
                                    right_min_around_len)
    res_set = re.findall(pattern, one_page_source, re.DOTALL)
    for res in res_set:
        left = res[0]
        right = res[1]
        around_content = AroundContent(left, right)
        around_contents.append(around_content)
    return around_contents