from numpy import *
from numpy.linalg import*
matriz=array(eval(input("digite a matriz de notas: ")))
a=int(input("numero de aluno: "))
c = matriz.shape [1]
s= sum(matriz[a,:])	
media= s/c
print(round(media,2))