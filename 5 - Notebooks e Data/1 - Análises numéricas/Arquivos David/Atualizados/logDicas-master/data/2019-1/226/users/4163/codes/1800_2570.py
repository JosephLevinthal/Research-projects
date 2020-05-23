from numpy import*

n = array(eval(input("digite: ")))

aux = 1
m =sum(n)/size(n)


for i in range(size(n)):
	a = 0
	a = a + abs(n[i]-m)
	aux = aux * a
	
p = aux**(1/size(n))
print(round(p, 3))
	