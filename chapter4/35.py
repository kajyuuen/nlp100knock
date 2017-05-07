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

max_len = 0
max_index = 0
index_count = -1
tmp_index = 0

for text_list in make_text_lists():
    for morpheme in text_list:
        index_count += 1
        if morpheme['pos'] == '名詞':
            if tmp_index == 0:
                tmp_len = 1
                tmp_index = index_count
            else:
                tmp_len += 1
        else:
            if tmp_len > max_len:
                max_len = tmp_len
                max_index = tmp_index
            tmp_index = 0

index_count = 0
for text_list in make_text_lists():
    for morpheme in text_list:
        index_count += 1
        if max_index < index_count and index_count <= max_index + max_len:
            print(morpheme['surface'], end=' ')
