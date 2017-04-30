f = open('hightemp.txt','r')
lines = f.readlines()
f.close()

for line in lines:
    line = line.replace('\t',' ')
    print(line, end='')
