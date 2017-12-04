1
word = input()
n = -1
for piece in word:
    print(word[:n])
    n = n - 1
2
word = input()
n = 1
for piece in word:
    print(word[:n])
    n = n + 1

3
word = input()
n = 0
for letter in word:
    print(word[n:] + word[0:n])
    n = n + 1

4
word = input()
n = 0
for letter in word:
    print(word[n:] + word[:n])
    n = n - 1

5
word = input()
n = -1
for letter in word:
    print(word[n:])
    n = n - 1
6
word = input()
n = 0
for letter in word:
    print(word[n:])
    n = n + 1

7
word = input()
n = 1
m = -1
for letter in word:
    print(word[n:m])
    n = n + 1
    m = m - 1

