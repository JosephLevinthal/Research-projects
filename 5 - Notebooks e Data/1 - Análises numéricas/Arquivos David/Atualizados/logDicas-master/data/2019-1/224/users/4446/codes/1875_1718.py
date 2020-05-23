from numpy import *
from numpy.linalg import *

tab=array(eval(input("digite a matriz que representa o tab: ")))
l=int(input("digite a linha: "))
c=int(input("digite a coluna: "))

if (tab[l,c]== 'P'):
	print("PRETA")
if (tab[l,c]== 'B'):
	print("BRANCA")
if (tab[l,c]== 'V'):
	print("VAZIA")