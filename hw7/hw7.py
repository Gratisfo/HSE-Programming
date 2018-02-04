def words_from_file(filename):
    ''' Читает текст и разделяет его на слова'''
    with open (filename, encoding = 'utf-8') as f:
        text = f.read()        
    words = text.split()
    return words

def adj_counter(words):
    ''' Создает список прилагательных на ous '''
    adj = []
    for word in words:
        if word[-3:] == 'ous':
            adj.append(word)
    return adj

def len_counter(adj):
    ''' Подсчитывает среднюю длину прилагательных из списка'''
    sum_len = 0
    for a in adj:
        sum_len = sum_len + len(a) #Сумма всех длин
    average = sum_len//len(adj) #Длина на колличество слов в списке
    return average
       


def main():
    words = words_from_file('text.txt')
    adjectives = adj_counter(words)
    print('Колличество прилагательных на ous:',len(adjectives))
    length = len_counter(adj_counter(words))
    print('Их средняя длина:', length)
    
if __name__ == '__main__':
    main()
