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
  
