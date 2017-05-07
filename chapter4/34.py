import re

def make_text_lists():
    f = open('neko.txt.mecab','r')
    lines = f.readlines()
    f.close()

    text_list = []
    text_lists = []

    for line in lines:
        if line != 'EOS\n':
            morpheme = re.split('[,\t]', line)
            morpheme_dic = {'surface':morpheme[0], 'base':morpheme[7], 'pos':morpheme[1], 'pos1':morpheme[2]}
            text_list.append(morpheme_dic)
        else:
            text_lists.append(text_list)
            text_list = []
    return text_lists

def ngram(n,data):
    ngram_list = []
    for i in range(len(data)-n+1):
        ngram = []
        for j in range(i,n+i):
            ngram.append(data[j])
        ngram_list.append(ngram)
    return ngram_list

def print_check_noun(three_morphemes):
    if three_morphemes[0]['pos'] == '名詞' and three_morphemes[1]['surface'] == 'の' and three_morphemes[2]['pos'] == '名詞':
        print(three_morphemes[0]['surface'] + three_morphemes[1]['surface'] + three_morphemes[2]['surface'])

for text_list in make_text_lists():
    three_morphemes_list = ngram(3, text_list)
    for three_morphemes in three_morphemes_list:
        print_check_noun(three_morphemes)
