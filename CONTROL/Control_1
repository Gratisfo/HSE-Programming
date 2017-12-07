with open ('freq.txt', encoding ='utf-8') as f:
    lines = f.readlines()
    for line in lines:
        cells = line.split()
        if len(cells) >= 4 and cells[4] == 'перех':
            voc.append(cells)
            y = ' '.join(cells)
            print(y)
