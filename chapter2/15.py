head = int(input())
count = 1

f = open('hightemp.txt','r')
lines = f.readlines()
f.close()

for line in reversed(lines):
    print(line, end='')
    if count < head:
        count += 1
    else:
        break
