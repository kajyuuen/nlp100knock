import re

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

class Chunk:
    def __init__(self):
        self.morphs = []
        self.dst = -1
        self.srcs = []

    def print_morphs(self):
        surface = ''
        for morph in self.morphs:
            surface += morph.surface
        return surface

def make_chunks_lists():
    f = open('neko.txt.cabocha','r')
    lines = f.readlines()
    f.close()

    count = 0
    chunks_list = []
    chunks_lists = []
    chunks = {}
    morpheme_list = []
    idx = -1

    for line in lines:
        if line == 'EOS\n':
            count += 1
            if len(chunks) > 0:
                for k, chunk in sorted(chunks.items()):
                    # print(chunk.print_morphs()+'\tsrcs:'+str(chunk.srcs)+'\tdst:'+str(chunk.dst))
                    chunks_list.append(chunk)
                chunks_lists.append(chunks_list)
                chunks_list = []
            chunks = {}
        elif line != 'EOS\n':
            morpheme = re.split('[,\s{1}]', line)
            if morpheme[0] != '*':
                if morpheme[0] == '':
                    morpheme_object = Morph(morpheme[0], morpheme[8], morpheme[2], morpheme[3])
                else:
                    morpheme_object = Morph(morpheme[0], morpheme[7], morpheme[1], morpheme[2])
                chunks[idx].morphs.append(morpheme_object)
            elif morpheme[0] == '*':
                cols = re.split('\s', line)
                idx = cols[1]
                # * ID 係り先のID 主辞/機能語の位置と任意の個数の素性列  主辞/機能語の位置と係り関係のスコア
                # 係り先のID dst
                dst = re.search(r'(.*?)D', cols[2]).group(1)
                if idx not in chunks:
                    chunks[idx] = Chunk()
                chunks[idx].morphs = morpheme_list
                chunks[idx].dst = dst
                if dst != '-1':
                    if dst not in chunks:
                        chunks[dst] = Chunk()
                        chunks[dst].srcs.append(int(idx))
                morpheme_list = []

    return chunks_lists

for i, chunks_list in enumerate(make_chunks_lists()):
    if i == 8:
        for chunk in chunks_list:
            if chunk.dst != -1:
                print(chunk.print_morphs()+'\tsrcs:'+str(chunk.srcs)+'\tdst:'+str(chunk.dst))
        break
