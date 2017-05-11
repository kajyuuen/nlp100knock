import re

def make_line(line):
    pattern = re.compile('(^.*?[\.|\;|\:|\?|\!])\s([A-Z].*)')
    line = line.strip()
    if len(line) > 0:
        match = pattern.match(line)
        if match:
            print(match.group(1))
            make_line(match.group(2))
        else:
            print(line)

f = open('nlp.txt','r')
lines = f.readlines()
f.close()

for line in lines:
    make_line(line)
