import re

f = open('britain-text.txt','r')
text = f.read()
f.close()
tmp_dic = {}

r = re.compile(r'\{\{基礎情報(.+)\n\}\}\n', re.MULTILINE | re.S)
tmp_list = r.search(text).group(1).split('\n|')

r = re.compile(r'(.+)=(.+)', re.MULTILINE | re.S)
for tmp in tmp_list:
    m = r.match(tmp)
    if m:
        tmp_dic[m.group(1).replace(' ','')] = m.group(2)

print(tmp_dic)
