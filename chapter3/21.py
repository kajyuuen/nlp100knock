f = open('britain-text.txt','r')
text = f.read()
f.close()

lines = text.split('\n')

for line in lines:
    if 'Category' in line:
         print(line)
