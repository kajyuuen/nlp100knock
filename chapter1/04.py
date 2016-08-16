test = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
data = test.replace('.','').split()
head = [1,5,6,7,8,9,15,16,19]
dic = {} 
for i in range(len(data)):
    if i + 1 in head:
        dic[data[i][0]] = i
    else:
        dic[data[i][0:2]] = i
print(dic)
