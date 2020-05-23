from numpy import *
from numpy.linalg import *

vet = array(eval(input("a: ")))


a = zeros((3,3), dtype=int)
b = zeros((1,3), dtype=int)


for i in range(a):
	for j in range(a):
		if a[i] == 0:
			if a[j] == 0:
				vet[0]= vet[0] - 2
				a[0,0] = a[0,0] + 2
			elif a[j] == 1: 
				vet[1] = vet[1] - 1
				a[0,1] = a[0,1] + 1
			elif a[j] == 2:
				vet[2] = vet[2] - 4
				a[0,2] = a[0,2] + 4
		elif a[i] == 1:
			if a[j] == 0:
				vet[0]= vet[0] - 1
				a[1,0] = a[1,0] + 1
			elif a[j] == 1: 
				vet[1] = vet[1] - 2
				a[1,1] = a[1,1] + 2
		elif a[i] == 2 :
			if a[j] == 0:
				vet[0]= vet[0] - 2
				a[2,0] = a[2,0] + 2
			elif a[j] == 1: 
				vet[1] = vet[1] - 3
				a[2,1] = a[2,1] + 3
			elif a[j] == 2:
				vet[2] = vet[2] - 2
				a[2,2] = a[2,2] + 2
b[0] = sum((a[0,:]))
b[1]= sum((a[1,:]))
b[2]= sum((a[2, :]))
print("estafilococo: ", b[0])
print("salmonela: ", b[1])
print("coli: ", b[2])
if (b[0] < b[1]) and (b[0] < b[1]):
	print("estafilococo")
elif (b[1] < b[0])and(b[1] < b[2]):
	print("salmonela")
elif (b[2] < b[0]) and (b[2] < b[1]):
	print("coli")
