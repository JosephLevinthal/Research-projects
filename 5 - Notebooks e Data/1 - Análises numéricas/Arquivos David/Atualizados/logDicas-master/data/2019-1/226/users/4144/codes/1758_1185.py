from numpy import *
a = array(eval(input("qtd de glicose: ")))
i = 0
ocorr = 0
while(i < size(a)):
	if(a[i]>99):
		print(i)
		ocorr = ocorr + 1
	i = i + 1
print(ocorr)