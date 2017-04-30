f = open('hightemp.txt','r')
lines = f.readlines()
f.close()

unique_pref = set()

for line in lines:
    line_septab = line[:-1].split('\t')
    unique_pref.add(line_septab[0])

print(unique_pref)
