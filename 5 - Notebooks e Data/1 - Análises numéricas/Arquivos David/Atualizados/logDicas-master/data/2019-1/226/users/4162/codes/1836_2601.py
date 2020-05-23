"""
Lab 07 – Exercicio 01
@author: IComp / UFAM
SISTEMAS DE EQUACOES LINEARES -- FRUTAS
"""

from numpy import *
from numpy.linalg import *

# Matriz do sistema linear (informado no enunciado)
frutas = array([[3,12,1], [12,0,2], [0,2,3]])

# Vetor de constantes (informado no enunciado)
compras = array([23.6, 52.6, 27.7])
compras = compras.T

# Resolucao do sistema de equacoes lineares
preco = dot(inv(frutas),compras)

print(preco)