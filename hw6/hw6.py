import random
def open_file(filename):
    with open (filename, encoding = 'utf - 8') as b:
        text = b.read()
        words = text.split()
        return words
    
def noun_1():
    nouns = open_file('noun_1.txt')
    return random.choice(nouns)

def adjective(word):
    adjectives = open_file('adjective.txt')
    return random.choice(adjectives) + ' ' + word

def adverb():
    adverbs = open_file('adv_2.txt')
    return random.choice(adverbs)

def intensifier(adv):
    intensifier = open_file('adv_1.txt')
    random_intensifier = random.choice(intensifier)
    result = adv + ' ' + random_intensifier
    return result

def verb_1(subj):
    verbs = open_file('verb_1.txt')
    return subj + ' ' + random.choice(verbs)

def part_1(f_part):
    noun_1ACC = open_file('noun_1ACC.txt')
    return f_part + ' ' + random.choice(noun_1ACC)

def noun_2():
    nouns = open_file('noun_2.txt')
    return random.choice(nouns) 

def verb_2(subj):
    verbs = open_file('verb_2.txt')
    return subj + ' ' + random.choice(verbs)

def part_2(s_part):
    noun_2ACC = open_file('noun_2ACC.txt')
    return s_part + ' ' + random.choice(noun_2ACC) + '.'

def union(sent_1, sent_2):
    unions = open_file('unions.txt')
    return sent_1 + ', ' + random.choice(unions) + ' ' + sent_2

def random_sentence():
    sentence = union(part_1(verb_1(adjective(noun_1())+ ' ' + intensifier(adverb()))), part_2(verb_2(noun_2())))
    return sentence

def main():
    print(random_sentence())
    print()
    num_of_sents = random.randint(1, 15) 
    for i in range(num_of_sents):  
        sentence = random_sentence() 
        sentence = sentence.capitalize() 
        print(sentence, end=' ') 

main()
