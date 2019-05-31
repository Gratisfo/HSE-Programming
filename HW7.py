
# coding: utf-8

# In[2]:


import re
import gensim
import logging
import pandas as pd
import urllib.request
from gensim.models import word2vec


# In[3]:


urllib.request.urlretrieve("http://rusvectores.org/static/models/rusvectores2/ruscorpora_mystem_cbow_300_2_2015.bin.gz", "ruscorpora_mystem_cbow_300_2_2015.bin.gz")


# In[4]:


m = 'ruscorpora_mystem_cbow_300_2_2015.bin.gz'

if m.endswith('.vec.gz'):
    model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=False)
elif m.endswith('.bin.gz'):
    model = gensim.models.KeyedVectors.load_word2vec_format(m, binary=True)
else:
    model = gensim.models.KeyedVectors.load(m)


# In[33]:


#задаем поле
beruf = ['учитель_S']
berufs = []


# In[34]:


for word in beruf:
    # проверяем наличие слова в модели 
    if word in model:
        print(word)
        # смотрим на вектор слова 
        print(model[word][:10])
        # выдаем 10 ближайших соседей слова:
        for i in model.most_similar(positive=[word], topn=10):
            # слово + коэффициент косинусной близости
            print(i[0], i[1])
            if i[1] >0.5:
                berufs.append(i[0])
        print('\n')
    else:
        # Увы!
        print('Увы, слова "%s" нет в модели!' % word)             
print(berufs)


# In[36]:


edges = []
for b in berufs:
    edge = (b, beruf[0])
    print(edge)
    edges.append(edge)
print(edges)


# In[37]:


import networkx as nx


# In[52]:


G = nx.Graph()
G.add_nodes_from(beruf)
G.add_edges_from(edges)


# In[53]:


print('узлы', G.nodes())
print('рёбра', G.edges())


# In[54]:


import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot') 

# для начала надо выбрать способ "укладки" графа. Их много, возьмём для начала такой:
pos=nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_color='red', node_size=50) # рисуем узлы красным цветом, задаём размер узла
nx.draw_networkx_edges(G, pos, edge_color='yellow') # рисуем рёбра жёлтым
plt.axis('off') # по умолчанию график будет снабжён осями с координатами, здесь они бессмысленны, так что отключаем
plt.show() # что получилось?


# In[55]:


nx.draw_networkx_nodes(G, pos, node_color='red', node_size=3) 
nx.draw_networkx_edges(G, pos, edge_color='yellow')
nx.draw_networkx_labels(G, pos, font_size=10, font_family='Arial')
plt.axis('off') 
plt.show()


# In[ ]:


#shell_layout


# In[3]:


plain_text = 'Произвольность_S знака, по поводу которой мы выше допускали теоретическую возможность перемены. Углубляясь в вопрос, мы усматриваем, что в действительности самая произвольность знака защищает язык от всякой попытки, направленной к его изменению. Говорящая масса, будь она даже сознательнее, не могла бы обсуждать вопросы языка. Ведь для того чтобы подвергать обсуждению какую-либо вещь, надо, чтобы она отвечала какой-то разумной норме.'


# In[13]:


text = plain_text.split(' ')
print(text)


# In[21]:


text = ['Произвольность_S', 'знака_S', 'поводу_S', 'которой_P', 'мы_P', 'допускали_V', 'возможность_S', 'перемены_S', 'Углубляясь_V', 'в', 'вопрос,', 'мы', 'усматриваем,', 'что', 'в', 'действительности', 'самая', 'произвольность', 'знака', 'защищает', 'язык', 'от', 'всякой', 'попытки,', 'направленной', 'к', 'его', 'изменению.', 'Говорящая', 'масса,', 'будь', 'она', 'даже', 'сознательнее,', 'не', 'могла', 'бы', 'обсуждать', 'вопросы', 'языка.', 'Ведь', 'для', 'того', 'чтобы', 'подвергать', 'обсуждению', 'какую-либо', 'вещь,', 'надо,', 'чтобы', 'она', 'отвечала', 'какой-то', 'разумной', 'норме.']
   


# In[ ]:


обозначаем части речи пропустить через y_morphy


# In[ ]:


Взять слово, опредлить все слова которые втречаются на рассмотянии 3 от него и провести свзяь


# In[26]:


new_prof = []
for word in prof:
    # проверяем наличие слова в модели 
    if word in model:
        print(word)
        # смотрим на вектор слова 
        print(model[word][:10])
        # выдаем 10 ближайших соседей слова:
        for i in model.most_similar(positive=[word], topn=10):
            # слово + коэффициент косинусной близости
            print(i[0], i[1])
            if i[1] >0.5:
                new_prof.append(i[0])
        print('\n')
    else:
        # Увы!
        print('Увы, слова "%s" нет в модели!' % word)
              
print(new_prof)
for i in new_prof:
    prof.append(i)
print(prof)

