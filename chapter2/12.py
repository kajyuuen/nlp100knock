f = open('hightemp.txt','r')
lines = f.readlines()
f.close()

col1 = open('col1.txt', 'w')
col2 = open('col2.txt', 'w')
for line in lines:
    line_septab = line[:-1].split('\t')
    col1.write(line_septab[0]+'\n')
    col2.write(line_septab[1]+'\n')
