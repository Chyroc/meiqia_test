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


def deal_player_name_file():
    file_name = 'hupu/name_word.txt'
    players_name_dict = {}
    all_players_list = []
    with open(file_name, encoding='utf-8') as f:
        for name in f:
            full_name = name.split(',')[0]
            for i in re.split(',| |-', name.replace('\n', '')):
                players_name_dict[i] = full_name
                all_players_list.append(i)
    return players_name_dict, all_players_list


def get_once_names(all_players_list):
    return [i for i in all_players_list if all_players_list.count(i) == 1]


def cut_players_name_word(all_players_list):
    for i in set(all_players_list):
        jieba.add_word(i)
    split_words = analyse.extract_tags(content, topK=None, withWeight=True)
    return dict([i for i in split_words if i[0] in set(all_players_list)])


def fix_name_belong_one_person(players_name_words, once_name_words, players_name_dict):
    result = {}
    for k, v in players_name_words.items():
        if k in once_name_words:
            if not hasattr(result, players_name_dict[k]):
                result[players_name_dict[k]] = 0
            result[players_name_dict[k]] += v
        else:
            result[k] = v
    return sorted(list(result.items()), key=lambda k: k[1], reverse=True)


if __name__ == '__main__':
    content = merge_content()
    players_name_dict, all_players_list = deal_player_name_file()
    once_name_words = get_once_names(all_players_list)
    players_name_words = cut_players_name_word(all_players_list)

    result = fix_name_belong_one_person(players_name_words, once_name_words, players_name_dict)
    with open('result.json', 'w', encoding='utf-8') as f:
        json.dump(result[:100], f, ensure_ascii=False, indent=2)
