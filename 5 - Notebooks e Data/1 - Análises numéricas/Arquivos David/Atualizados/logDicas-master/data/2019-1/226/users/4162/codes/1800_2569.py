from numpy import*
x= array(eval(input("digite o vetor de numero real: ")))       
q = size(x)
m = sum(x)/q
d = 0
for g in range(size(x)):
	d = d+(x[g]-m)**2/(q-1)
d = d**(1/2)	
print(round(d, 3))