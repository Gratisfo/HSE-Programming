voc = []
bigvoc = []
with open ('freq.txt', encoding ='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        cells = line.split()
        voc.append(cells[0])
        bigvoc.append(cells)
words = []
while True:
    word = input()
    if word == '':
        break
    else:
        words.append(word)
for w in words:
    if w in voc:
        for b in bigvoc:
            if b[0] == w:
                print("Морф.призн слова", '"', w, '":', ', '.join(b[2:-2]),'; ' 'ipm:', ' '.join(b[-1:]))
    else:
        print('В словаре нет слова:', w)

