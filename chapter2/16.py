n = int(input())
count = 0

f = open('hightemp.txt','r')
lines = f.readlines()
f.close()

split_size = int(len(lines)/n)

for line in lines:
    print(line, end='')
    if count < split_size - 1:
        count += 1
    else:
        count = 0
        print()
