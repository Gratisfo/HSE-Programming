import re

def openfile(filename):
    with open (filename, encoding='utf-8') as f:
        text = f.read()
        
    return text


def findwords(text):
    words = []    
    #прошедшедшее время
    verb1 = re.findall('съел[оаи]?с?ь?', text)
    words.append(verb1)
    #будущее ед.ч, инф., повелительное накл., деепр
    verb2 = re.findall('съе[мшсв][ьт]?(?:те|ь|ся)', text)
    words.append(verb2)
    #будущее мн.ч.
    verb3 = re.findall('съеди?(?:те|м|ят)', text)
    words.append(verb3)
    #причастия действ., страд., полн. и крат. формы
    verb4 = re.findall('съевш[иеау][йгмехяю].?', text)
    words.append(verb4)
    verb5 = re.findall('съеденн?[ыоау][йгмяюех]?.?', text)
    words.append(verb5)

    return words

def un_list(wlist):
    result = []
    for word in wlist:
        for w in word:
            if w not in result:                 
                result.append(w) #список с неповторяющимися формами
    
    return result
   
def main():
    filename = input('Введите имя файла: ')
    text = openfile(filename)
    tokens = findwords(text)
    results = ' '.join(un_list(tokens))
    print('Формы глагола "съесть":',results)
    

if __name__ == '__main__':
    main()
        
