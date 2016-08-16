import random

def typo(text):
    data = text.split()
    ans = []
    for i in range(len(data)):
        if len(data[i]) > 4:
            lists = list(data[i][1:-1])
            ans.append(data[i][0] + ''.join(random.sample(lists,len(lists))) + data[i][-1:])
        else:
            ans.append(data[i])
    return ' '.join(ans)

text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(typo(text))
