import os
import csv
import random
import pinyin as pin
from playsound import playsound
from gtts import gTTS
# https://pypi.org/project/pinyin/


class VocabList(list):
    def input_zh_char(self):
        while True:
            # [zh_char入力画面]
            # if True: # 中国語入力終了ボタンが押される
            #     break
            print('入力を続けますか？Y/N')
            select = input()
            if select == 'N':
                break
            print('漢字を入力してください。')
            zh_char = input()
            self.append({'zh_char': zh_char})
    def check_pinyin(self):
        for vocab_num in range(len(self)):
            pinyin = pin.get(self[vocab_num]['zh_char'])
            # [zh_charとpinyinを表示して合ってるか聞く]
            print('拼音はあっていますか？')
            print(self[vocab_num]['zh_char'] + ': ' + pinyin)
            select = input()
            if select == 'n': 
                num_pinyin = pin.get(self[vocab_num]['zh_char'], format='numerical')
                # [編集可能な形で表示して入力してもらう]
                num_pinyin = input()
                pinyin = no_num_pinyin(num_pinyin)
            self[vocab_num]['pinyin'] = pinyin
    def input_meaning(self):
        for vocab_num in range(len(self)):
            # [zh_char(とpinyin)を表示して入力してもらう]
            print('日本語を入力してください。')
            print(self[vocab_num]['zh_char'] + ': ')
            meaning = input()
            self[vocab_num]['meaning'] = meaning
    # def pronounce(self, vocab_num):

def no_num_pinyin(num_pinyin): #str
    pinyin = num_pinyin
    return pinyin

def csv_to_mp3(filename): #str
    with open('./imported_csv/'+filename+'.csv') as f:
        index = ['zh_char', 'pinyin', 'meaning']
        reader = csv.reader(f)
        vocab_list = [dict(zip(index, row)) for row in reader]
        os.makedirs('./pronounce/'+filename)
        for vocab_num in range(len(vocab_list)):
            tts = gTTS(text=vocab_list[vocab_num]['zh_char'], lang='zh-cn')
            tts.save('./pronounce/'+filename+'/'+str(vocab_num)+'.mp3')

def csv_shuffle_read(filename): #str
    with open('./imported_csv/'+filename+'.csv') as f:
        index = ['zh_char', 'pinyin', 'meaning']
        reader = csv.reader(f)
        pure_list = [dict(zip(index, row)) for row in reader]
        random_order = random.sample(range(len(pure_list)), len(pure_list))
        vocab_list = VocabList()
        vocab_list += [dict(zip(index, pure_list[num])) for num in random_order]
    return vocab_list, random_order

def csv_make(vocab_list, filename): # VocabList, str
    with open('./imported_csv/'+str(filename)+'.csv', 'x') as f:
        writer = csv.writer(f)
        for vocab_num in range(len(vocab_list)):
            writer.writerow([vocab_list[vocab_num]['zh_char'], 
                vocab_list[vocab_num]['pinyin'], 
                vocab_list[vocab_num]['meaning']])

vocab = VocabList()
vocab.input_zh_char()
vocab.check_pinyin()
vocab.input_meaning()
csv_make(vocab, 'test')
csv_to_mp3('test')