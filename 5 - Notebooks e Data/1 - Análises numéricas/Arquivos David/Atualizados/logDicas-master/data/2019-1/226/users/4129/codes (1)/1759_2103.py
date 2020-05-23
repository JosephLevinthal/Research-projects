from numpy import*

A = array(eval(input("Vetor A:")))
B = array(eval(input("Vetor B:")))

i = 0
x = -1
b = zeros(size(B), dtype=int )
while(i < size(B)):
	b[i] = B[x]
	x = x - 1
	i = i + 1
i = 0
while(i < size(A)):
	if(b[i]>=A[i]):
		print(b[i])
	else:
		print(A[i])
	i = i +1

