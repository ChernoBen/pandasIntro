# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 14:24:45 2020

@author: benja
"""
import json
import numpy as np
import pandas as pd
from pandas.io.json import json_normalize

'''
dataframe to html
criando uma tabela em um arquivo html
'''
frame = pd.DataFrame(np.random.random((4,4)),
                     index = ['white','black','red','blue'],
                     columns = ['up','down','right','left'])

s = ['<html>']
s.append('<head><title>My dataframe</title></head>')
s.append('<body>')
s.append(frame.to_html())
s.append('</body></html>')
html = ''.join(s)
html_file = open('myFrame.html','w')
html_file.write(html)
html_file.close()

'''
processo inverso
'''
web_frames = pd.read_html('myFrame.html')
'''
webframes é uma lista de dataframes
'''
#############
'''
obtendo dataframe a partir de pagina web
'''

ranking = pd.read_html('https://www.meccanismocomplesso.org/classifica-punteggio/')
print(ranking[0])

'''
criando json de um df
'''
dframe = pd.DataFrame(np.arange(16).reshape(4,4),
                      index = ['white','black','red','blue'],
                      columns = ['up','down','right','left'])
dframe.to_json('dframe.json')

'''
lendo json
'''
jsonfile = pd.read_json('dframe.json')

'''
normalização de json
'''
file = open('books.json','r')
text = file.read()
text = json.loads(text)
#agora normalizar
final_json  = json_normalize(text,'books')
'''basicamente essa função cria uma tabela com o conteudo de todos elementos que tiverem *books como chave '''
final_json = json_normalize(text,'books',['nationality','writer'])#adicionando chaves do mesmo levl de books

