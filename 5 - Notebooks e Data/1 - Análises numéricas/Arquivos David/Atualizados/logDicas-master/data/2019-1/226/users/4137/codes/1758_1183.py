from numpy import*

x = array(eval(input("Escreva um vetor:")))

i = 0
p = 0 #numeros positivos
n = 0 #numeros negativos

while(i < size(x)):
	if(x[i] < 0):
		n = n + 1
	i = i + 1	

tf = size(x) - n

vt = zeros(tf, dtype=int)

i = 0
s = 0

while(i < size(x)):
	if(x[i]>=0):
		vt[s] = x[i]
		s = s+1
	i = i + 1
print(vt)