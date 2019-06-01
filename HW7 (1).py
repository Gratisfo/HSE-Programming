
# coding: utf-8

# In[2]:


import n


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


# In[62]:


flower = ['ромашка_S']


# In[72]:


edges = []
flower_1 = []
for word in flower:
    if word in model:
        print(word) 
        print(model[word][:10])
        for i in model.most_similar(positive=[word], topn=10):
            print(i[0], i[1])
            edge = (word, i[0])
            edges.append(edge)
            flower_1.append(word)
            flower_1.append(i[0])
            if i[1] >0.5:
                print(i[1])
                print(model[i[0]][:10])
                for m in model.most_similar(positive=[i[0]], topn=10):
                    print(m[0], m[1])
                    edge_new = (i[0], m[0])
                    edges.append(edge_new)
                    flower_1.append(m[0])
            
    else:
        # Увы!
        print('Увы, слова "%s" нет в модели!' % word)
        
print(edges)
print(flower_1)


# In[73]:


import networkx as nx


# In[75]:


G = nx.Graph()
G.add_nodes_from(flower_1)
G.add_edges_from(edges)


# In[76]:


print('узлы', G.nodes())
print('рёбра', G.edges())


# In[77]:


import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot') 

# для начала надо выбрать способ "укладки" графа. Их много, возьмём для начала такой:
pos=nx.spring_layout(G)

nx.draw_networkx_nodes(G, pos, node_color='red', node_size=50) # рисуем узлы красным цветом, задаём размер узла
nx.draw_networkx_edges(G, pos, edge_color='yellow') # рисуем рёбра жёлтым
plt.axis('off') # по умолчанию график будет снабжён осями с координатами, здесь они бессмысленны, так что отключаем
plt.show() # что получилось?


# In[79]:


nx.draw_networkx_nodes(G, pos, node_color='red', node_size=3) 
nx.draw_networkx_edges(G, pos, edge_color='yellow')
nx.draw_networkx_labels(G, pos, font_size=7, font_family='Arial')
plt.axis('off') 
plt.show()


# In[80]:


#degree centrality
deg_flower = nx.degree_centrality(G)
i = 0
for nodeid in sorted(deg_flower, key=deg_flower.get, reverse=True):
    i += 1
    print(nodeid, round(deg_flower[nodeid], 3))
    if i == 10:
        break


# In[81]:


bc_flower = betweenness_centrality(G)
print(bc_flower)


# In[83]:


a = betweenness_centrality_subset(G, G.nodes(), targets, normalized=False, weight=None)

