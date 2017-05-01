import re

f = open('britain-text.txt','r')
text = f.read()
f.close()

lines = text.split('\n')

for line in lines:
    if 'File' in line:
        print(line.split('|')[0].replace('[[File:',''))
