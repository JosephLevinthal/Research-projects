from numpy import*

v= array(eval(input("Vetor: ")))
n = size(v)

for i in range(size(v)):
	m = ((sum(v[i])**2) /n)**1/2
	i = i +1
x = round(m,n)		  
print(x)


