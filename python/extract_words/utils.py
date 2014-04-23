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
    This function is used to get around content between keyword.

    Example
    -------
    >>> one_page_source = "1111ddd2222edde3333"
    >>> left_min_around_len = 2
    >>> right_min_around_len = 3
    >>> key_word = "dd"
    >>> ret = get_around_one_keyword_pattern(one_page_source,
    ...                                      key_word,
    ...                                      left_min_around_len,
    ...                                      right_min_around_len)
    >>> print("We found " + str(len(ret)) + " keywords in page source.")
    We found 2 keywords in page source.
    >>> for around_keyword in ret:
    ...     print("'" + key_word + "' is located between '" +
    ...           around_keyword.left +
    ...           "' and '" +
    ...           around_keyword.right + "'")
    ...
    'dd' is located between '11' and 'd22'
    'dd' is located between '2e' and 'e33'
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


def get_around_keywords_pattern(one_page_source,
                                key_words,
                                left_min_around_len,
                                right_min_around_len):
    """
    Example
    -------
    one_page_source = "1111ddd2222eeee3333"
    left_min_around_len = 2
    right_min_around_len = 3
    key_words = ["11", "22"]
    around_contents_list = get_around_keywords_pattern(one_page_source,
                                                       key_words,
                                                       left_min_around_len,
                                                       right_min_around_len)
    for i in xrange(len(key_words)):
        key_word = key_words[i]
        around_contents = around_contents_list[i]
        for around_content in around_contents:
             for around_keyword in around_content:
                 print("'" + key_word + "' is located between '" +
                       around_keyword.left +
                       "' and '" +
                       around_keyword.right + "'")
    """
    around_contents_list = []
    for key_word in key_words:
        around_contents = get_around_one_keyword_pattern(one_page_source,
                                                         key_word,
                                                         left_min_around_len,
                                                         right_min_around_len)
        around_contents_list.append(around_contents)
    return around_contents_list