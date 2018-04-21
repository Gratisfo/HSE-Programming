import os

file_list = os.listdir()
print(file_list) #Список содержимого в папке

def short_name(flist):
    dirs = 0 #папки
    one_word = 0 #папки с одним словом в названии
    for file in flist:
        if '.' not in file: #Нет расширения => папка
            dirs += 1
            if ' ' in file.lower(): #Есть пробелы в названии => больше одного слова
                one_word += 1
    if dirs > 0:
        if one_word > 0:
            print("Количество папок, в названии которых больше одного слова:", one_word)
        else:
            print('Названия всех папок состоят из одного слова')
    else:
        print('В данной папке нет других папок')        
        
def main():    
    short_name(file_list)
    
if __name__ == '__main__':
    main()
