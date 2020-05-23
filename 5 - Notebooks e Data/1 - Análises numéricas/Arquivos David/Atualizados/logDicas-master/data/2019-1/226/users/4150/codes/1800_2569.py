from numpy import*

x = array(eval(input("digite: ")))

m = sum(x)/size(x)

aux = 0

for i in range(size(x)):
	 aux = aux + (x[i]-m)**2

d = round((aux/(size(x)-1))**(1/2),3)
print(d)
	