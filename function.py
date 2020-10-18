import os
import csv
import random
import pinyin as pin
from playsound import playsound
from gtts import gTTS
# https://pypi.org/project/pinyin/


def no_num_pinyin(num_pinyin):  # str
    pinyin = num_pinyin
    return pinyin
    


def csv_to_mp3(filename):  # str
    with open('./imported_csv/'+filename+'.csv', 'r', encoding='utf-8_sig') as f:
        reader = csv.reader(f)
        vocab_list = [row for row in reader]
        os.makedirs('./pronounce/'+filename)
        for vocab_num in range(len(vocab_list)):
            tts = gTTS(text=vocab_list[vocab_num]['zh_char'], lang='zh-cn')
            tts.save('./pronounce/'+filename+'/'+str(vocab_num)+'.mp3')


def csv_shuffle_read(filename):  # str
    with open('./imported_csv/'+filename+'.csv', 'r', encoding='utf-8_sig') as f:
        reader = csv.reader(f)
        pure_list = [row for row in reader]
        random_order = random.sample(range(len(pure_list)), len(pure_list))
        vocab_list = []
        vocab_list += [pure_list[num] for num in random_order]
    return vocab_list, random_order


def csv_make(vocab_list, filename):  # VocabList, str
    with open('./imported_csv/'+str(filename)+'.csv', 'x', encoding='utf-8_sig') as f:
        writer = csv.writer(f)
        for vocab_num in range(len(vocab_list)):
            writer.writerow([vocab_list[vocab_num][0],
                             vocab_list[vocab_num][1],
                             vocab_list[vocab_num][2]])

# vocab = VocabList()
# vocab.input_zh_char()
# vocab.check_pinyin()
# vocab.input_meaning()
# csv_make(vocab, 'test')
# csv_to_mp3('test')
