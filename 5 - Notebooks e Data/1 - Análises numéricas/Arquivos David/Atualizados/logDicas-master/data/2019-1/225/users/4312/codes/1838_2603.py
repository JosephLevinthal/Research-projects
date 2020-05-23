from numpy import*
from numpy.linalg import*
#vetor = array(eval(input("Insira a matriz: ")))
vetor = [[1,10,100,1000],[2,20,200,2000],[3,30,300,3000],[4,40,400,4000]]
vetor = sorted(vetor, reverse=True)#sorted.vetor(reverse=True)
print (vetor)
matriz = zeros((4,4), dtype = int)
w=0
while(size(vetor)>w):
	matriz[w]=matriz[w] + vetor[w]
	w+=1
#for i in range(vetor):
#	for j in range(vetor):
#		if (vetor[i] < vetor[1] and vetor[i] < vetor [2] and vetor[i] < vetor [3]):
#			 matriz = vetor[0]
#		elif (vetor[i] > vetor[0] and vetor[i] < vetor[2] and vetor[i] < vetor[3]):
#			matriz = vetor[1]
#		elif (vetor[i] > vetor[0] and vetor[i] > vetor[1] and vetor[i] < vetor[3]):
#			matriz = vetor[2]
#		elif(vetor[i] > vetor[0] and vetor[i] > vetor[1] and vetor[i] > vetor[2]):
#			matriz = vetor[3]
		
print(matriz)