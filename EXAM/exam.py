import os
import re
import collections

def task_1(path):
    files = [files for root, dirs, files in os.walk(path)]
    with open('information.csv', 'w', encoding='utf-8') as f_w:
        f_w.write("doc_id\ttitle\tauthor\tcreated\ttopic\ttagging\n")
        for f in files[0]:
            with open(os.path.join(path, f), encoding='cp1251') as f_r:
                for a in f_r:
                    if '/head' in a:
                        break
                    if re.search (r'<meta content="(.*?)" name="docid"></meta>', a):
                        doc_id = re.search(r'<meta content="(.*?)" name="docid"></meta>', a).groups()[0]
                    if re.search(r'<title>(.*?)</title>', a):
                        title = re.search(r'<title>(.*?)</title>', a).groups()[0]
                    if re.search(r'<meta content="(.*?)" name="author"></meta>', a):
                        author = re.search(r'<meta content="(.*?)" name="author"></meta>', a).groups()[0]                        
                    if re.search(r'<meta content="(.*?)" name="created"></meta>', a):
                        created = re.search(r'<meta content="(.*?)" name="created"></meta>', a).groups()[0]
                    if re.search(r'<meta content="(.*?)" name="topic"></meta>', a):
                        topic = re.search(r'<meta content="(.*?)" name="topic"></meta>', a).groups()[0]
                    if re.search(r'<meta content="(.*?)" name="tagging"></meta>', a):
                        tagging = re.search(r'<meta content="(.*?)" name="tagging"></meta>', a).groups()[0]
                 
                f_w.write(doc_id + '\t' + title + '\t' + author + '\t' + created + '\t' + topic + '\t' + tagging  + '\n')

def task_2(path):
    files = [files for root, dirs, files in os.walk(path)]
    n_dict = collections.Counter()
    with open('abbr.csv', 'w', encoding='utf-8') as f_w:
        f_w.write("аббревиатура\tколичество вхождений\n")
        abbrev = []
        for f in files[0]:
            with open(os.path.join(path, f), encoding='cp1251') as f_r:
                for a in f_r:
                    if re.search(r'lex="(.*?)"', a):
                        if re.search(r'lex="(.*?)"', a).groups()[0].isupper():
                            if 'XX' not in (re.search(r'lex="(.*?)"', a).groups()[0]):
                                abbrev.append(re.search(r'lex="(.*?)"', a).groups()[0])
        freq = collections.Counter(abbrev)
        for abb in freq:
            a = abb + '\t'+ str(freq[abb]) + '\n'
            f_w.write(a)

def main():
    first = task_1('news')
    second = task_2('news')

if __name__ == '__main__':
    main()
