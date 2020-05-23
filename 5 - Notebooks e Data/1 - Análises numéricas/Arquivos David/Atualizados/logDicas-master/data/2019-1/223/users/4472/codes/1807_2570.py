from numpy import*

x = array(eval(input("Numeros: ")))
n = size(x)
m = mean(x)
p = 1
for i in range(size(x)):
	ab = abs(x[i] - m)
	p = p * ab
	
k = (p)**(1/n)
print(round(k,3))