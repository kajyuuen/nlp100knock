import json

f = open('jawiki-country.json','r')
lines = f.readlines()
f.close()

f = open('britain-text.txt', 'w')

for line in lines:
    data = json.loads(line)
    if data['title'] == 'イギリス':
        f.write(data['text'])
