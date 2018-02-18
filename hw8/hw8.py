def intro():
    print("Привет! Поиграй со мной. Угадай, какое слово пропущенно!")
    
def open_file(filename):
    ''' открывает файл '''
    with open (filename, encoding = 'utf - 8') as f:
        lines = f.readlines()
    return lines

def clue(raw_lines):
    ''' делит строки на слова и создает словарь '''
    game = {}
    clue = []
    for line in raw_lines:
        line = line.strip('\n')
        line = line.split(',')
        word = line[0] #первое слово каждой строки будет ключом
        clue = line[1:] #все остальные - его элементами, заключенные в список
        game[word] = clue
           
    return game

def key_words(dict_game):
    n = 0
    num_try = 0
    
    for key in dict_game:
        print('"', dict_game[key][n], '..."') #Выводит первую подсказку       
        print('Введи пропущенное слово:')
        answ = input()
        while n <= 3: #Пока есть подсказки
            if answ == key: #Если пользователь угадал
                num_try = num_try + 1 #Считает кол-во попыток
                print('Верно! Использовано попыток', num_try, 'из 3')
                num_try = 0
                n = 0 #Обнуляем кол-во подсказок и попыток
                break
            else:
                if n <2: #Если еще остались подсказки
                    n = n + 1
                    num_try = num_try + 1
                    print( 'Использовано попыток', num_try,  'из 3')                
                    print('Неверно, попоробуй еще раз','"', dict_game[key][n], '...', '"')                    
                    answ = input()          
                else:
                    print( 'Использовано попыток', num_try + 1,  'из 3')
                    print('С этим словом не выходит', '\n')
                    n = 0
                    num_try = 0
                    break             
     
    print('Слова закончились. Конец!')
          

def main():
    greeting = intro()
    raw_data = open_file('Words.csv')
    all_words = clue(raw_data)
    game = key_words(all_words)
    
if __name__ == '__main__':
    main()
