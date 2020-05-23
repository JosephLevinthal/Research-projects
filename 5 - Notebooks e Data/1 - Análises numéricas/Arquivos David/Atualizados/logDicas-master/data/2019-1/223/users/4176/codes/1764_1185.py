from numpy import*

NG = array(eval(input('Entrada: ')))
			  
i = 0
n = 0
			  
while(i < size(NG)):
	if(NG[i] > 99 ):
		print(i)
		n = n + 1
	i = i + 1
print(n)