1
with open ('text.txt', encoding = 'utf-8') as f:
    text = f.read()
lines = text.splitlines() #Большой список, элементы - строки
print(lines)
x = 0
y = 0
for line in lines: #Для каждого элемента списка (строки)
    word = line.split() #Список - слова из каждой строки
    print(word, len(word)) #Список слов в строке, кол-во слов (длина списка)
    x += len(word) #Количество слов
    y += 1 #Количество строк
print(x //y) #среднее число слов в строке

2
with open ('text.txt', encoding = 'utf-8') as f:
    text = f.read()
lines = text.splitlines()
print(lines)
for line in lines:
    words = line.split()
x = len((min(words, key=len)))
print(x, 'Длина минимальной строки')
y = len((max(words, key=len)))
print(y, 'Длина максимальной строки')
if x ==0:
    print('Нельяз делить на ноль')
else:
    print(y//x)

3
x = 0
y = 0
with open ('text.txt', encoding = 'utf-8') as f:
    text = f.read()
    text = text.replace('.',' ').replace(',',' ').replace('?',' ').replace('\ufeff',' ').replace('!',' ').replace(':',' ').replace(';',' ').replace('"',' ').replace('(',' ').replace(')',' ')
    words = list(text.split()) #Разделили текст на слова и внесли их в список
for word in words:
    if len(word) > 3:
        x += 1
    elif len(word) == 1:
        y += 1
if y != 0:
    print('Слов длинее 3-х букв больше, чем слов длиной в 1 слово в ', x//y, 'раз/а')
else:
    print('Все слова длинее 1-ой буквы')

4
with open ('text.txt', encoding = 'utf-8') as f:
    text = f.read()
words = text.split()
z = 0
for word in words:
    if word.endswith('.') or word.endswith(',') :
        z += 1
print(round(100-z*100/71), '% от общего количества слов не оканчивается знаком препинания')
        
5
j = 0
with open('text.txt', encoding="utf-8") as f:
    text = f.read()
print(text)
splited_text = text.split()
print('Всего слов:', len(splited_text))
for w in splited_text:
    if len(w)>10:
        j = j +1
print('Слов, длинее 10-ти букв: ', j)
p = (j/len(splited_text))*100
print(round(p),'%')

6
j = 0
with open('text.txt', encoding="utf-8") as f:
    text = f.read()
words = text.split()
print('Всего слов:', len(words))
for word in words:
    for letter in word:
        if letter.isupper():
            j += +1
print('Слов с заглавной буквой: ', j)
print(round((j/len(words))*100), '%')


7
j = 0
with open('text.txt', encoding="utf-8") as f:
    text = f.read()
lines = text.splitlines()
print('Всего строк:', len(lines))
for line in lines:
    if len(line)>5:   
        j += +1
print('Строк, длинее 5-ти слов: ', j)
print(round((j/len(lines))*100), '%')

    
