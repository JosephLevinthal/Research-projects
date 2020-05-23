from numpy import*

Vetor = array(eval(input("entrada: ")))

i = 0
n = 0

while(i < size(Vetor)):
	if(Vetor[i] > 99):
		print(i)
		n = n +1
	i = i + 1
print(n)