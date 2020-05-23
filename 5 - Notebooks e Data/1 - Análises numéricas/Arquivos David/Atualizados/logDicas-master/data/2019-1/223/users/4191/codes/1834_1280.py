from numpy import *
from numpy.linalg import *

matriz=array(eval(input("Matriz: ")))
jogadas=input("Jogadas: ")

moeda=0
life=100

linha=0
coluna=0

for i in jogadas:
	
	if(matriz[linha,coluna]<0)or(matriz[linha,coluna]>shape(matriz)[0])or(matriz[linha,coluna]>shape(matriz)[1]):
		matriz[linha-1,coluna-1]=matriz[linha-1,coluna-1]
	if(i=='A'):		
		coluna=coluna-1
	elif(i=='D'):
		coluna=coluna+1
	elif(i=='W'):
		linha=linha-1
	elif(i=='S'):
		linha=linha+1
		
	if(matriz[linha,coluna]==0):
		matriz[linha,coluna]=matriz[linha,coluna]
	elif(matriz[linha,coluna]==11):
		moeda=moeda+1
	elif(matriz[linha,coluna]==22):
		life=life-5
	elif(matriz[linha,coluna]==33):
		matriz[linha,coluna]=matriz[linha-1,coluna-1]
		
print("posicao x: ", linha)
print("posicao y: ", coluna)
print("moedas: ", moeda)
print("life: ", life)		