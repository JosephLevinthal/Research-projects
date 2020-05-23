from numpy import *
vetor = array(eval(input("digite o diametro das batatas: ")))
i = 0
a = 0
b = 0
c = 0
while(i<size(vetor)):
	if(vetor[i] >= 10):
		a = a + 1
	if(5 <= vetor[i] < 10):
		b = b + 1
	if(vetor[i] < 5):
		c = c + 1
	i = i + 1
print(a)
print(b)
print(c)