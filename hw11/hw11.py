import re

def open_file(fname):
    with open (fname, encoding = "utf-8") as f:
        text = f.read()

    return text

def replace_word(text):
    new_text_1 = re.sub('динозавр', 'кот', text)
    new_text_2 = re.sub('Динозавр','Кот', new_text_1)    

    return new_text_2

def create_newfile(page):
    with open ('Коты.html', 'w', encoding = 'utf-8') as f:
        f.write(page)        

def main():
    filename = open_file('Динозавры.html')
    changed = replace_word(filename)
    new_file = create_newfile(changed)


if __name__ == '__main__':
    main()
