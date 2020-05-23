from numpy import *
n = int(input("insira o numero:"))
i = 0
v = zeros(n,dtype =int)




if(n==2):
	v = arange(n)
elif(n > 2):
	while(i < size(n)):
		v[n] = v[i] - i
		i = i + 1

	
print(v[i])