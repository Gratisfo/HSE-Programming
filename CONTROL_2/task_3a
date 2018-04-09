import re
import collections
def open_file(fname):
  ''' Открывает и читает файл '''
  with open (fname, encoding = 'utf-8') as f:
    text = f.read()
  return text

def find_adj(text):
  adjectives = re.findall(r'type="l.f.{3}"', text)
  #Находит нужные прилагательные
  adj = collections.Counter(adjectives)
  #Подчсчитывает и создает частотный словарь
  with open ('result_3.txt', 'w', encoding='utf-8') as f:
    for key in sorted(adj, key = adj.get):
      a = key + " - " +str(adj[key])+ '\n'
      f.write(a)
  #Записывает в файл
      
def main():
  get_text = open_file('corpus.xml')
  adj = find_adj(get_text)
 

if __name__ == '__main__':
    main()
