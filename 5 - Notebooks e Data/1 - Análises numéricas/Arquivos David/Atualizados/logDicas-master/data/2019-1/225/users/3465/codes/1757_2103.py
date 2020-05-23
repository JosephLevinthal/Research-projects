from numpy import *
A = array(eval(input("")))
B = array(eval(input("")))
B = B[::-1]
for i in range(len(A)):
	if A[i]>B[i]:
		print(A[i])
	else:
		print(B[i])