import re
import collections

def get_data(file_name):
    ''' прочесть содержимое файла '''
    with open(file_name, encoding='utf-8') as f:
        raw_text = f.read()
    return raw_text

def lexeme(text):
    '''Среднее кол-во разборов на слово'''
    all_ana = re.findall(r'<ana lex="\w*?" gr=".*?" />', text) #кол-во <ana>
    all_lemm = re.findall(r'\<w>.*?(\w*?)</w>', text)#кол-во <w>
    #print(len(all_ana) / len(all_lemm)) #среднее 

def freq_d(text):
    '''Составляет частотный словарь частей речи'''
    pos = re.findall(r'gr="(\w*)?[=,]', text)
    pos_d = collections.Counter(pos)       
    #pos_d = {p: pos.count(p) for p in pos} #частотный словарь
    
    with open ('exam_w.txt', 'w', encoding = 'utf-8') as f:
        f.write("POS\tFrequency\n")
        for p in pos_d:
            a = p+ '\t'+ str(pos_d[p]) + '\n'
            f.write(a)

def find_INS(text):
    splitted_lines = text.split('\n')
    #print(splitted_lines[:10])
    #marker_instr = re.findall(r'gr="S.*?вин', line)
    for line in splitted_lines:
        if re.findall(r'gr="S,.*?твор', line):
            word = re.findall(r'\<w>.*?(\w*?)</w>', line)
            print(word)
    

if __name__ == '__main__':
    raw = get_data("text.xml")
    amount = lexeme(raw)
    frequancy = freq_d(raw)
    instrumentalis = find_INS(raw)
    
