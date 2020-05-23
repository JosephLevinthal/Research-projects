from numpy import*

matriz = array(eval(input("Leia: ")))

for i in range(shape(matriz)[0]):
	print(max(matriz[i,:]))