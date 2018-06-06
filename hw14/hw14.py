import re
import collections
from collections import Counter

def get_text(file):
    with open(file) as f:
        text = f.read()    
    return text

def clean_text(text):
    sentences = re.compile('[.!?]').split(text) #разделяет текст на предложения
    clear_sent = [re.sub('[\n«»—,:;"]', '', sent) for sent in sentences] #чистит от знаков препинания
    #print(clear_sent[:10])
    return clear_sent

def reduplication(sentences):
   
    for sent in sentences[:10]: #Делит предложениe на слова, переводит в нижний регистр
        if sent:            
           words = sent.lower().split()
           new_sent = []
    
           for word in words: 
                freq = Counter(word) #Подсчитывает частотность слов           
                new_letters = [letter*freq[letter] for letter in word] #умножает буквы               
                new_word = ''.join(new_letters)+ " " #Склеивает буквы в слово
                new_sent.append(new_word) #Добавляет в список слова                                  
           new_sent = ''.join(new_sent)     
           print(new_sent[0].upper() + new_sent[1:-1] + '.')#C заглавной буквы и точкой #Без проела перед ней
           
def main():
    open_file = get_text(input('Введите имя файла:'))    
    sentences = clean_text(open_file)
    papaya = reduplication(sentences)
     
    
if __name__ == '__main__':
    main()
