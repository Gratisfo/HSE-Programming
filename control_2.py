voc = []
y = ''
with open ('freq.txt', encoding ='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        cells = line.split()
        if cells[2] == "част":
            voc.append(cells[0])
            y = cells[0] + ','
            print(y)
print(len(voc))
