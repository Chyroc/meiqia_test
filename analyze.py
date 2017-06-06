# -*- coding: utf-8 -*-
import os
import re
import json

import jieba
from jieba import analyse


def merge_content():
    root_dir = 'hupu/data'
    content_list = []
    for i in os.listdir(root_dir):
        with open(os.path.join(root_dir, i)) as f:
            content_list.append(f.read())
    return ' '.join(content_list)


def get_name_words():
    file_name = 'hupu/name_word.txt'
    name_words = []
    with open(file_name, encoding='utf-8') as f:
        for name in f:
            name_words.extend(re.split(',| |-', name.replace('\n', '')))
    return name_words


if __name__ == '__main__':
    content = merge_content()
    name_words = get_name_words()

    for i in name_words:
        jieba.add_word(i)
    split_words = analyse.extract_tags(content, topK=None, withWeight=True)
    players_name = [i for i in split_words if i[0] in name_words]

    # result
    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(players_name[:100], f, ensure_ascii=False, indent=2)
