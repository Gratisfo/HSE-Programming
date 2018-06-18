import re
import collections

SYMBS = "1234567890,—[]↑№!\"\'«»?.,;:|/\+*{}<>@#$%-^& )("

def read(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        text = f.read()
    return text

def clean(text):
    words = []
    text = text.strip().lower().split()
    for word in text:
        if word:
            words.append(word.strip(SYMBS))
    return words

def dictionary(words):
    counter = collections.Counter(words)
    return counter

def write(d):
    table = []
    with open('result.txt', 'w', encoding='utf-8') as t:
        for word in sorted(d, key=d.get, reverse=True):
            table.append(word + '\t' + str(d[word]))
        table = '\n'.join(table)
        t.write(table)

def main():
    return write(dictionary(clean(read('text.txt'))))

if __name__ == "__main__":
    print(main())

## https://pythonworld.ru/moduli/modul-collections.html
## https://habrahabr.ru/post/349860/#Ispolzovanie_dopolnitelnyh_flagov_v_pitone
