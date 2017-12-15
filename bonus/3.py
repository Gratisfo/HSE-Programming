vow = ['e', 'y', 'u', 'i', 'o', 'a']
cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z']
words = input()
if words != '':
    words = words.split()
    for word in words:
        if word[0] in vow:
           print(word + 'ay')
        elif word[0] and word[1] in cons and word[2] in vow:
            print(word[2:] + word[0:2] + 'ay')
        elif word[0] in cons and word[1] in vow:
            print(word[1:] + word[0] + 'ay')
        elif word[0]and word[1] and word[2] in cons:
            print(word[3:] + word[0:3] + 'ay')
else:
    print('слов нет!')

