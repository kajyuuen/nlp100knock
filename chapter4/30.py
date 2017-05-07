import re

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
