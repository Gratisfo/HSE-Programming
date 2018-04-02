import re

def open_file(filename):
    with open (filename, encoding="utf-8") as f:
        text = f.read()
    return text

def find_kind(text):
    kind = re.findall('Семейство.*?title.*?>(.*?)</a>', text)
    return kind

def main():
    filename = input('Введите имя файла без разрешения файла: ')
    code = open_file(filename+".html")    
    family = find_kind(code)
    if family:
        print(family[0])
    else:
        print('У этого вида нет категории семейства')

if __name__ == '__main__':
    main()

