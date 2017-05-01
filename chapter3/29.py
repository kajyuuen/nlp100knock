import re
import requests

f = open('britain-text.txt','r')
text = f.read()
f.close()
tmp_dic = {}

r = re.compile(r'\{\{基礎情報(.+)\n\}\}\n', re.MULTILINE | re.S)
tmp_list = r.search(text).group(1).split('\n|')

r = re.compile(r'(.+)=(.+)', re.MULTILINE | re.S)

internal_link = re.compile(r'\[{1,2}(.+)\]{1,2}')
for tmp in tmp_list:
    m = r.match(tmp)
    if m:
        # m.group(2)を処理していく
        field = re.sub(r'\'{2,5}','',m.group(2))
        # \1,\2で後方参照を行う
        field = re.sub(r"\[{2}([^|\]]+?\|)*(.+?)\]{2}", r'\2', field)
        tmp_dic[m.group(1).replace(' ','')] = field

url = 'https://en.wikipedia.org/w/api.php'

params = { 'action':'query',
           'titles': 'File:{}'.format(tmp_dic['国旗画像']),
           'prop': 'imageinfo',
           'format': 'json',
           'iiprop': 'url'}

json_data = requests.get(url, params=params).json()

print(json_data['query']['pages']['23473560']['imageinfo'][0]['url'])
