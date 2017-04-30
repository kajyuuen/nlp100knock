count = 0

f = open('hightemp.txt','r')
lines = f.readlines()
f.close()

for line in lines:
    count += 1

print(count)
