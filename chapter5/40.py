import re
import time

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

def make_text_lists():
    f = open('neko.txt.cabocha','r')
    lines = f.readlines()
    f.close()

    text_list = []
    text_lists = []

    for line in lines:
        if line != 'EOS\n':
            morpheme = re.split('[,\s{1}]', line)
            if morpheme[0] != '*':
                if morpheme[0] == '':
                    morpheme_object = Morph(morpheme[0], morpheme[8], morpheme[2], morpheme[3])
                else:
                    morpheme_object = Morph(morpheme[0], morpheme[7], morpheme[1], morpheme[2])
                text_list.append(morpheme_object)
        else:
            text_lists.append(text_list)
            text_list = []
    return text_lists

make_text_lists()

for i, text_list in enumerate(make_text_lists()):
    if i == 2:
        for morpheme in text_list:
            print(morpheme.surface+','+morpheme.base+','+morpheme.pos+','+morpheme.pos1)
