from numpy import*

x = array(eval(input("Vetor: ")))
n = size(x)
m = sum(x)/n
d = 0

for g in range(size(x)):
	d = d+(x[g]-m)**2/(n-1)
d = d**(1/2)	
	
print(round(d, 3))