def cipher(char):
    ans = ''
    for i in range(len(char)):
        if char[i].islower():
            ans += chr(219-ord(char[i]))
        else:
            ans += char[i]
    return ans

text = input()

print(cipher(text))
print(cipher(cipher(text)))
