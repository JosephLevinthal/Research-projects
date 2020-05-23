from numpy import *
A = array(eval(input("digite o vetor A: ")))
B = array(eval(input("digite o vetor B: ")))
ib = 0
z = zeros(size(B), dtype = int)
#inverte as linhas do vetor B
while(ib<size(B)):
	z[ib] = B[-1*(ib+1)]
	ib = ib + 1
#################################
i = 0
while(i<size(A)):
	if(A[i]>z[i]):
		print(A[i])
	else:
		print(z[i])
	i = i + 1
