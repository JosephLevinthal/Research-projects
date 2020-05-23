from numpy import*

n = array(eval(input("Numeros:")))
for i in range(size(n//2)):
	j = size(n)-1-i
	aux = n[i]
	n[i] = n[j]
	n[j] = aux
print(n)