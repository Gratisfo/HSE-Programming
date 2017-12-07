pred = []
s = 0
with open('freq.txt', encoding = 'utf-8') as f:
    lines = f.readlines()
    for line in lines[:]:        
        #line - Просто строки        
        cells = line.split()
        if cells[2] == 'част':
            pred.append(cells[0])
            s += float(cells[-1])
y = ', '.join(pred)
print(y, '\n', 'Сумма ipm:', s)
