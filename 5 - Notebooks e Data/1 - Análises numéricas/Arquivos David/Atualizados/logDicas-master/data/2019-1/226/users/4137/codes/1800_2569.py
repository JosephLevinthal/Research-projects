from numpy import*

x = array(eval(input("Numeros reais:")))
d = 0
m = sum(x)/size(x)
for i in range(size(x)):
	d = d + (x[i]-m)**2/(size(x)-1)
d = d**(1/2)
print(round(d,3))