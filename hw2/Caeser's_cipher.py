#Caesar's cipher
alpha = ' абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
n = int(input())
s = input()
res = ''
for letter in s:
    res += alpha[(alpha.index(letter) + n)]
print('Result: ', res)











    
