import os

start_path = '.' #Путь к папке, в которой находится программа
raw_file = [] #Пустой спиок для файлов

def find_files(path):
    '''Ищет все фалы в папках'''
    for dies, root, files in os.walk(start_path):
        for file in files:
            raw_file.append(file)
    #print(raw_file)        
    return raw_file

fnames = [] #Список для имен файлов

def names_list(names):
    for file in raw_file:
        name = os.path.splitext(file)[0] #Отделяет расширение файла от названия
        if name not in fnames:
            fnames.append(name)
    #print(fnames)
    print('Колличество разных фаулов в папках, без учета расширения:', len(fnames))
        
def main():
    files = find_files(start_path)
    clean_names = names_list(files)    
    
if __name__ == '__main__':
    main()    
