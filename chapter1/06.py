def ngram(flag,n,word):
    if flag == 0: #単語gram
        data = word.replace('.','').split()
    else: #文字gram
        data = list(word)
    ans_list = []
    for i in range(len(data)-n+1):
        gram = []
        for j in range(i,n+i):
            gram.append(data[j])
        if flag == 0:
            print('-'.join(gram))
        else:
             ans_list.append(''.join(gram))
    return ans_list

str1 = "paraparaparadise"
str2 = "paragraph"

X = set(ngram(1,2,str1))
Y = set(ngram(1,2,str2))
print(X|Y) #和集合
print(X&Y) #積集合
print(X-Y) #差集合1
print(Y-X) #差集合2
print('se' in X )
print('se' in Y )

