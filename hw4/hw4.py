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
        
#Запятая, стоящая рядом со словом, будет засчитываться в его длину.
#Одиночные символы будут считаться, как отдельные слова
#Можно было бы пересичлить все в .replase() или .isalpha(), но у меня не получилось
