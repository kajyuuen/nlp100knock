import re

f = open('britain-text.txt','r')
text = f.read()
f.close()

lines = text.split('\n')

for line in lines:
    m = re.match('\[\[Category:([^\|]+)(\|?.+)\]\]', line)
    if m:
        print(m.group(1))
