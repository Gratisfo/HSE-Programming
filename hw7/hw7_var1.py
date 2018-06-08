import re
import collections
def open_file(filename):
  with open (filename, encoding = 'utf-8') as f:
    text = f.read()
  text = re.sub('[\n«»—,:;"]', ' ', text) 
  return text  

def clean_text(text):
  words = text.lower().split()
  ing_words = [word for word in words if word[-3:] == 'ing']
  return (ing_words)

def freq_words(words):
  freq = collections.Counter(words)
  print(freq)
  return freq

def user_word(word, freq):
  if word in freq:
    print(word, freq[word])


def main():    
    get_text = open_file('eng_text.txt')
    words = clean_text(get_text) 
    frequancy = freq_words(words)
    output = user_word(input('Enter the word'), frequancy)

if __name__ == '__main__':
    main()
