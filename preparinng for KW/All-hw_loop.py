1
word = input('Введите слово: ')
for letter in word[1::2]:
    if letter != 'к' and letter != 'а':
        print(letter)
2
word = input()
for letter in word[0::1]:
    if letter =='о' or letter == 'е' or letter == 'п':
        print(letter)
3
word = input()
for letter in word[::-1]:
    if letter !='з' and letter !='я':
        print(letter)
4
num = int(input('Введите число: '))
print(num)
q = 0
while num != q:
    word = input('Введите слово: ')
    print(word)
    if word == 'программирование':
        break
    else:
        q = q + 1
        print('End')
5
word = input()
s = len(word) // 2
for letter in word[:s]:
    print(letter)
for letter in word[len(word): s-1 : -1]:
        print(letter)

6
num = int(input())
q = 1
while q < 11:
    print(q, '*', num, '=', num * q)
    q = q + 1

7
num = int(input())
n = 0
while 2**n <= num:
    print(2**n)
    n = n + 1
            

