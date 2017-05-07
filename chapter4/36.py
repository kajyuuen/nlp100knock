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

word_dic = {}

for text_list in make_text_lists():
    for morpheme in text_list:
        if morpheme['pos'] == '名詞':
            word_dic[morpheme['surface']] = word_dic.get(morpheme['surface'], 0) + 1

for k, v in reversed(sorted(word_dic.items(), key=lambda x:x[1])):
    print(k+':'+str(v))
