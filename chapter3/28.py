import re

f = open('britain-text.txt','r')
text = f.read()
f.close()
tmp_dic = {}

r = re.compile(r'\{\{基礎情報(.+)\n\}\}\n', re.MULTILINE | re.S)
tmp_list = r.search(text).group(1).split('\n|')

r = re.compile(r'(.+)=(.+)', re.MULTILINE | re.S)

# 処理するための正規表現
internal_link = re.compile(r'\[{1,2}(.+)\]{1,2}')
for tmp in tmp_list:
    m = r.match(tmp)
    if m:
        # m.group(2)を処理していく
        field = re.sub(r'\'{2,5}','',m.group(2))
        # \1,\2で後方参照を行う
        field = re.sub(r"\[{2}([^|\]]+?\|)*(.+?)\]{2}", r'\2', field)
        tmp_dic[m.group(1).replace(' ','')] = field

for i, v in tmp_dic.items():
    print(i+':'+v)
