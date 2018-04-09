import re
def open_file(fname):
  ''' Открывает и читает файл '''
  with open (fname, encoding = 'utf-8') as f:
    text = f.read()
  return text

def count_stripes(text):
  '''Подсчитывает строки между <se> и <\se> и записывает их в файл'''
  num_str = re.findall(r".*\n",text)
  print(num_str)
  num_str = len(re.findall(r".*\n",text))
  
  with open ('result_1.txt', 'w', encoding = 'utf-8') as f:
    f.write(str(num_str))
    
def main():
  get_text = open_file('corpus.xml')
  count = count_stripes(get_text)
 

if __name__ == '__main__':
    main()
