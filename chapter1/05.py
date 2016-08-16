
def ngram(flag,n,word):
    if flag == 0: #単語gram
        data = word.replace('.','').split()
    else: #文字gram
        data = list(word)
    for i in range(len(data)-n+1):
        gram = []
        for j in range(i,n+i):
            gram.append(data[j])
        if flag == 0:
            print('-'.join(gram))
        else:
            print(''.join(gram))

text = "I am an NLPer"
ngram(0,2,text)
print('---------------')
ngram(1,2,text)
