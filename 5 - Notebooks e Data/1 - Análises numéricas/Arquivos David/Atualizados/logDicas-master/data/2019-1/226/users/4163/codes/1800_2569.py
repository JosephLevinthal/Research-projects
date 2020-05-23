from numpy import*
n = array(eval(input("digite: ")))

a = 0
m =(sum(n)/size(n))

for i in range(size(n)):
			 
	a = a + (n[i]-m)**2
	d = (a /(size(n)-1))**0.5
print(round(d, 3))
