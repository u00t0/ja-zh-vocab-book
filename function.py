import os
import csv
import random
import pinyin as pin
from playsound import playsound
from gtts import gTTS


# def csv_to_mp3(filename):
#     with open('./imported_csv/'+filename+'.csv', 'r', encoding='utf-8_sig') as f:
#         reader = csv.reader(f)
#         vocab_list = [row for row in reader]
#         os.makedirs('./pronounce/'+filename)
#         for vocab_num in range(len(vocab_list)):
#             tts = gTTS(text=vocab_list[vocab_num][0], lang='zh-cn')
#             tts.save('./pronounce/'+filename+'/'+str(vocab_num)+'.mp3')


def csv_shuffle_read(filename):
    with open('./imported_csv/'+filename+'.csv', 'r', encoding='utf-8_sig') as f:
        reader = csv.reader(f)
        pure_list = [row for row in reader]
        random_order = random.sample(range(len(pure_list)), len(pure_list))
        vocab_list = []
        vocab_list += [pure_list[num] for num in random_order]
    return vocab_list, random_order


def csv_make(vocab_list, filename):
    with open('./imported_csv/'+str(filename)+'.csv', 'x', newline='', encoding='utf-8_sig') as f:
        writer = csv.writer(f)
        for vocab_num in range(len(vocab_list)):
            writer.writerow([vocab_list[vocab_num][0],
                             vocab_list[vocab_num][1],
                             vocab_list[vocab_num][2]])
