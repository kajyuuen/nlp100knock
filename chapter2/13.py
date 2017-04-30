col1 = open('col1.txt', 'r')
col1_lines = col1.readlines()
col1.close()

col2 = open('col2.txt', 'r')
col2_lines = col2.readlines()
col2.close()

for (line1, line2) in zip(col1_lines, col2_lines):
    print(line1.replace('\n','')+'\t'+line2.replace('\n',''))
