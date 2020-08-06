# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 19:49:51 2020

@author: benja
"""
import numpy as np


a = np.array([1,2,3])
'''
definindo array multidimensional
'''
b = np.array([[1.3,2.4],[0.3,4.1]])
b.dtype
b.ndim #numero de dimensões
b.size #tamanho/quantidade de itens
b.shape # ex: (2,2) dois itens p/ 2

'''
definindo array de numeros complexos
'''
f = np.array([[1,2,3],[4,5,6]],dtype = complex)
'''
criando array de zeros
'''
np.zeros((3,3)) #3x3

'''
3 linhas e 4 colunas
'''
np.arrange(0,12).reshape(3,4)
'''
pegar o valor ente n e n
'''
np.linspace(0,10,5)