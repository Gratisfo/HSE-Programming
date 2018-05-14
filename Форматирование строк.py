>>> sq_again = [i**2 for i in [1, 2, 3, 4]]
>>> sq_again
[1, 4, 9, 16]
>>> text = [word.title() for word in 'на улице жара'.split()]
>>> text
['На', 'Улице', 'Жара']
>>> [sym+' ' for sym in 'abcdef']
>>> ''.join([sym+' ' for sym in 'abcdef'])
'a b c d e f ' 
>>> new_dic = {i: i**2 for i in [1, 2, 3, 4]}
>>> new_dic
{1: 1, 2: 4, 3: 9, 4: 16}
>>> [(item[1], item[0])for item in new_dic.items()]
[(1, 1), (4, 2), (9, 3), (16, 4)]
>>> [item[::-1] for item in new_dic.items()]
[(1, 1), (4, 2), (9, 3), (16, 4)] #то же самое, что и строчка выше
>>> [i in range(10)]
[True]
>>> [i for i in range(10)]
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>> [i for i in range(3, 19, 2)]
[3, 5, 7, 9, 11, 13, 15, 17]
>>> [i for i in range(3, 19) if i%2 == 0]
[4, 6, 8, 10, 12, 14, 16, 18]
>>> [word for word in 'Orange me ich I'.split() if len(word)>3]
['Orange']
>>> [word if word.istitle() else '_'+word+'_' for word in 'Алиса в стране чудес'.split()]
['Алиса', '_в_', '_стране_', '_чудес_']
>>> [word for word in 'Маленькая уточка бежит по свежему лугу'.split() if len(re.findall('[ыаоэеуяию]', word, re.IGNORECASE)) >3]
['Маленькая']
>>> [word for word in 'Orange me ich I'.split() if len(word)>3]
['Orange']

>>>import re
def reverse_dict(old_dic):
    #генерируем словарь
    new_dic = {old_dic[k]: k for k in old_dic} #идем по ключам старого словаря}
    return new_dic

word_len = {word: len(word) for word in 'Алиса в стране чудес.'.split()}
print(word_len)

len_word = reverse_dict(word_len)

print(len_word)
#result
{'Алиса': 5, 'в': 1, 'стране': 6, 'чудес.': 6}
{5: 'Алиса', 1: 'в', 6: 'чудес.'}

>>> 'Length of words {} equal {}'.format('miracles', len('miracle'))
'Length of words miracles equal 7'

>>>def greetings():
    user_name = input('What is your name?')
    print('Hello, {}!'.format(user_name))
greetings()
#result
What is your name? Any
Hello,  Any!
>>>>>> "Word's {0} lenght equal {1}". format('miracle', len('miracle'))
"Word's miracle lenght equal 7"     
>>> "Word's {1} lenght equal {0}". format('miracle', len('miracle'))
"Word's 7 lenght equal miracle"

>>> '{:12}'.format('condizioner')
'condizioner '
>>> '{:_<12}'.format('condizioner')
'condizioner_'
>>> '{:_>12}'.format('condizioner')
'_condizioner'

>>> '{:0.3f}'.format(1.2345) #f - от float
'1.234   

>>> print('Result is {:0.3f}'.format(1.38365))
Result is 1.384
