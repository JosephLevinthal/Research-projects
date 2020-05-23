from numpy import *

g1 = array(eval(input("Gols do time: ")))
g2 = array(eval(input("Gols do time adversario: ")))
v = zeros(3, dtype=int) #Cria um vetor com elementos nulos #Ex: zeros(4)  =  [0, 0, 0, 0]
va = 0					#Dtype indica que tipo de entrada no vetor, no caso serão inteiras, então dtype=int
vb = 0
e = 0                          #Função range cria uma sequência de numeros inteiros. 
for i in range(size(g1)): 		#Ex: range(6) = [0, 1, 2, 3, 4, 5, 6]
	a = g1 [i] #Atribuindo a ao elemento de g1 na posição i
	b = g2 [i] #Atribuindo b ao elemento de g2 na posição i
	
	#Verificando quem fez mais gols e consequentemente ganhou
	if (a > b): 
		va = va + 1
	elif (b > a):
		vb = vb + 1
	elif (a == b):
		e = e + 1
	#Atribuindo os valores no vetor nulo
	v [0] = va
	v [1] = e
	v [2] = vb

print(v)
	