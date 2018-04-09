import re
import collections
def open_file(fname):
  ''' Открывает и читает файл '''
  with open (fname, encoding = 'utf-8') as f:
    text = f.read()
  return text

def create_dict(fname): 
  attributes = re.findall('w lemma=".*?" type="(.*?)"',fname)
  #Ищет грамматические признаки
  attributes = collections.Counter(attributes)
  #Создает частотный словарь
  with open ('result_2.txt','w', encoding = 'utf-8') as f:
    for key in sorted(attributes, key=attributes.get, reverse=True):
      a = key + ' '+ str(attributes[key])+ '\n'
      f.write(a)
  #Записывает в файл
    
def main():
  get_text = open_file('corpus.xml')
  freq = create_dict(get_text)
 

if __name__ == '__main__':
    main()
