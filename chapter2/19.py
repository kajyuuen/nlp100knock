import collections

f = open('hightemp.txt','r')
lines = f.readlines()
f.close()

pref_list = []

for line in lines:
    line_septab = line[:-1].split('\t')
    pref_list.append(line_septab[0])

count_dict = collections.Counter(pref_list)

for pref, num in count_dict.most_common():
    print(pref)
