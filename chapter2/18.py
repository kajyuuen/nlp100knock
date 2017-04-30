f = open('hightemp.txt','r')
lines = f.readlines()
f.close()

temperature_list = []

for line in lines:
    line_septab = line[:-1].split('\t')
    temperature_list.append(float(line_septab[2]))

print(sorted(temperature_list))
