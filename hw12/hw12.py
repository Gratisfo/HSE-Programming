import os

file_list = os.listdir()

def short_name(flist):
    dirs = [] #папки
    one_word = [] #папки с одним словом в названии
    for file in flist:
        if '.' not in file: #Нет расширения => папка
            dirs.append(file)
            if ' ' in file.lower(): #Есть пробелы в названии => больше одного слова
                one_word.append(file)
            if '_' in file.lower():
                one_word.append(file)
                
    if len(dirs) > 0:
        if len(one_word) > 0:
            print("Количество папок, в названии которых больше одного слова:", len(one_word), '\n', ', '.join(one_word))
        else:
            print('Названия всех папок состоят из одного слова')
    else:
        print('В данной папке нет других папок')        
        
def main():    
    short_name(file_list)
    
if __name__ == '__main__':
    main()
