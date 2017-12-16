voc = ["а", "у", "е", "ы", "а", "о", "э", "я", "и", "ю"]
word = input()
out = ""
for w in word:
    if w not in voc:
        out += w
    else:
        out += w + "c" + w
print(out)
