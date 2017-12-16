vow = ['e', 'y', 'u', 'i', 'o', 'a']
word = input()
out = ""
for w in word:
    if w not in vow:
        out += w
    else:
        out += w + "aig"
print(out)
