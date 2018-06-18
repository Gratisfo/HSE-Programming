import re

def clean(file):
    r = re.compile('[1234567890,—\[\]↑№!\"\'«»?.,;:-|/+*{}<>@#$%-^&()]')
    with open(file, 'r', encoding='utf-8') as f:
        text = f.read()
        text = re.sub(r, '', text)
    return text

print(clean('text.txt'))
