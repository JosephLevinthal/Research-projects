from numpy import*
v = array(eval(input("Vetor:")))
i =0 
b = size(v)
f=0
m=0
while (i<b):
	m= f + ((v[i]**2)/(b))**1/2
	i+=1
	f+=1
print(round(m,2))