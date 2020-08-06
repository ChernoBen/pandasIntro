# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 20:22:05 2020

@author: benja
"""

import pandas as pd
import numpy as np

'''
criando serie e adicionando indice
'''

s = pd.Series([12,-4,7,9],index=['a','b','c','d'])
'''valores maiores que:'''
print(s[s>8])

'''
lendo csv
'''
csvframe = pd.read_csv('C:/Users/benja/Desktop/databooks/data/ndarray/arquivos/ch05.csv',sep=',')

'''
especificando nomes dos labels do csv
 *note que white,red,green e etc, entrarao para a tabela como instancias 
'''
csvframe2 = pd.read_csv('C:/Users/benja/Desktop/databooks/data/ndarray/arquivos/ch05.csv',names = ['white','red','blue','green','animal'])

'''
definindo indices
'''
ch6 = pd.read_csv('C:/Users/benja/Desktop/databooks/data/ndarray/arquivos/ch06.csv',index_col=['color','status'])

'''
regExp to parse txt files
note que :
    \s+ indica separador == space
    
'''
reg = pd.read_csv('C:/Users/benja/Desktop/databooks/data/ndarray/arquivos/space.csv',sep='\s+',engine='python')

'''
separar por Non digit == \D+
'''
nonDig = pd.read_csv('C:/Users/benja/Desktop/databooks/data/ndarray/arquivos/nonDigit.csv',sep='\D+',header=None,engine='python')

'''
excluindo linhas desnecessarias em arquivo txt
nesse caso excluiremos as linhas 0,1,3,6
'''
textFile = pd.read_csv('C:/Users/benja/Desktop/databooks/data/ndarray/arquivos/logfile.txt',sep=',',skiprows=[0,1,3,6])

'''
dataframe to csv
'''
frame = pd.DataFrame(np.arange(16).reshape((4,4)),
                     index = ['red','blue','yellow','white'],
                     columns = ['ball','pen','pencil','paper'])


frame.to_csv('ch05_7.csv')
