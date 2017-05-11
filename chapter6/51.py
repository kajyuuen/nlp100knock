import re

def make_line(line):
    pattern = re.compile('(^.*?[\.|\;|\:|\?|\!])\s([A-Z].*)')
    line = line.strip()
    if len(line) > 0:
        match = pattern.match(line)
        if match:
            yield match.group(1)
            make_line(match.group(2))
        else:
            return line

def make_word(line):
    words = line.split(' ')
    for word in words:
        pattern = re.compile('[\(]*([a-zA-Z0-9]+)[\)|\,|\.]*')
        match = pattern.match(word)
        if match:
            yield match.group(1)

f = open('nlp.txt','r')
lines = f.readlines()
f.close()

for line in lines:
    for split_line in make_line(line):
        for split_word in make_word(split_line):
            print(split_word)
