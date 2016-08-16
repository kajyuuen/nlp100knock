text = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
data = text.split()
pi = []
for i in range(0,len(data)):
    pi.append(len(data[i]))
print(pi)
