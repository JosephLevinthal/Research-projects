from numpy import *
alf = array(eval(input("Digite as letras do alfabeto: ")))

n= size(alf)
print(n)
aux = array([])
i = 0
for i in range(size(n//2)):
	aux = alf[i]
	alf[i] = alf[(n-i)-1]
	alf[(n-i)-1] = aux
	i = i-1
print(alf)
	