from numpy import*
v = array(eval(input("v: ")))
i = 0
soma = 0
for i in range(size(v)):
	if v[i] < 5.0:
		soma = soma + v[i] 
		i = i + 1
		print(soma)
		
		