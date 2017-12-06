1
inp = []
while True:
    y = input('Enter the word:')
    if y == '':
        break
    else:
        inp.append(y)
out = []
for i in inp:
    i = i.replace(i[2], '')
    out.append(i)
x = '\n'.join(out)
with open ('bla.txt', "w", encoding = "utf-8") as f:
    f.write(x)

2
inp = []
while True:
    y = input('Enter the word:')
    if y == "":
        break
    else:
        inp.append(y)
out = []
for i in inp:
    if len(i)>5:
        out.append(i)
x = '\n'.join(out)
with open ('function.txt', 'w', encoding = 'utf-8') as f:
    f.write(x)

3
inp = []
while True:
    y = input('Enter the word:')
    if y == "":
        break
    else:
        inp.append(y)
out = []
n = 1
for i in inp:
    i = i.replace(i[0:n], '')
    n += 1
    out.append(i)
x = '\n'.join(out)
with open ('function.txt', 'w', encoding = 'utf-8') as f:
    f.write(x)

4
inp = []
while True:
    x = input('Введите латинское слово: ')
    if x == '': 
        break
    else: 
        inp.append(x)
out = []
n = []
for i in inp:
    if i[-2:] == "ri" or i[-2:] == "re" or i[-3:] == 'iri' or i[-4:] == 'isse' or i[-4:] == 'urus':
        out.append(i)
y = '\n'.join(out)
with open("function.txt", "w", encoding="utf-8") as f:
    f.write(y)
5
inp = []
while True:
    x = input('Введите латинское слово: ')
    if x == '': 
        break
    else: 
        inp.append(x)
out = []
for i in inp:
  if i[-3:] == "tur" or i[-4:] == "ntur":
    out.append(i)
y = '\n'.join(out)
with open("function.txt", "w", encoding="utf-8") as f:
    f.write(y)

6
num = []
n = 0
while n !=7:
    x = input()
    n += 1
    if x == '': 
        break
    else: 
        num.append(x)
stripes =[]
ind = 0
for i in num:
    ln = int(num[ind])
    if ln >= 0:
        stripe = ln*'X'        
        stripes.append(stripe)
    ind += 1
x = '\n'.join(stripes)
with open ('Fail.txt', 'w', encoding = 'utf-8') as f:
    f.write(x)

7
num = []
n = 0
while n != 8:
    x = input()
    n += 1
    if x == '': 
        break
    else: 
        num.append(x)
stripes =[]
m = 0
for i in num:
    if m > 7:
        break
    else:
        a = num[m] + num[m+1]
        stripes.append(a)
        m = m + 2 
x = '\n'.join(stripes)
with open ('Fail.txt', 'w', encoding = 'utf-8') as f:
    f.write(x)
    

    
