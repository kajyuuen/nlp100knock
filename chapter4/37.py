import matplotlib.pyplot as plt
import matplotlib as mpl
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

count = 0
y = []
label = []
for k, v in reversed(sorted(word_dic.items(), key=lambda x:x[1])):
    if count >= 10: break
    print(k+':'+str(v))
    y.append(v)
    label.append(k)
    count += 1

mpl.rcParams['font.family'] = 'AppleGothic'
x = range(10)
plt.bar(x, y, align="center")           # 中央寄せで棒グラフ作成
plt.xticks(x, label)  # X軸のラベル
plt.title('頻度上位10語')
plt.show()
