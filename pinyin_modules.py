import pinyin as pin
import re


def no_num_pinyin(num_pinyin):
    pinyin = ''
    pinyin_list = re.findall("\D*\d", num_pinyin)
    for pinyin_piece in pinyin_list:
        if 'a' in pinyin_piece:
            pinyin_piece = pinyin_change('a', re.search(
                '\d', pinyin_piece).group(), pinyin_piece)
        elif 'e' in pinyin_piece:
            pinyin_piece = pinyin_change('e', re.search(
                '\d', pinyin_piece).group(), pinyin_piece)
        elif 'o' in pinyin_piece:
            pinyin_piece = pinyin_change('o', re.search(
                '\d', pinyin_piece).group(), pinyin_piece)
        elif 'iu' in pinyin_piece:
            pinyin_piece = pinyin_change('u', re.search(
                '\d', pinyin_piece).group(), pinyin_piece)
        elif 'ui' in pinyin_piece:
            pinyin_piece = pinyin_change('i', re.search(
                '\d', pinyin_piece).group(), pinyin_piece)
        elif 'i' in pinyin_piece:
            pinyin_piece = pinyin_change('i', re.search(
                '\d', pinyin_piece).group(), pinyin_piece)
        elif 'u' in pinyin_piece:
            pinyin_piece = pinyin_change('u', re.search(
                '\d', pinyin_piece).group(), pinyin_piece)
        elif 'v' in pinyin_piece:
            pinyin_piece = pinyin_change('v', re.search(
                '\d', pinyin_piece).group(), pinyin_piece)
        pinyin += pinyin_piece
    return pinyin


def pinyin_change(char, num, string):
    string = re.sub(num, '', string)
    return re.sub(char, num_to_pinyin(char, num), string)


def num_to_pinyin(char, num):
    if char == 'a':
        if num == '0':
            return 'a'
        if num == '1':
            return 'ā'
        if num == '2':
            return 'á'
        if num == '3':
            return 'ǎ'
        if num == '4':
            return 'à'
    if char == 'i':
        if num == '0':
            return 'i'
        if num == '1':
            return 'ī'
        if num == '2':
            return 'í'
        if num == '3':
            return 'ǐ'
        if num == '4':
            return 'ì'
    if char == 'u':
        if num == '0':
            return 'u'
        if num == '1':
            return 'ū'
        if num == '2':
            return 'ú'
        if num == '3':
            return 'ǔ'
        if num == '4':
            return 'ù'
    if char == 'e':
        if num == '0':
            return 'e'
        if num == '1':
            return 'ē'
        if num == '2':
            return 'é'
        if num == '3':
            return 'ě'
        if num == '4':
            return 'è'
    if char == 'o':
        if num == '0':
            return 'o'
        if num == '1':
            return 'ō'
        if num == '2':
            return 'ó'
        if num == '3':
            return 'ǒ'
        if num == '4':
            return 'ò'
    if char == 'v':
        if num == '0':
            return 'ü'
        if num == '1':
            return 'ǖ'
        if num == '2':
            return 'ǘ'
        if num == '3':
            return 'ǚ'
        if num == '4':
            return 'ǜ'
