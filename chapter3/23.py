import re

f = open('britain-text.txt','r')
text = f.read()
f.close()

lines = text.split('\n')

for line in lines:
    if line.startswith('=='):
        print(line.replace('=','').replace(' ','')+':'+str(int(line.count('=')/2)-1))
