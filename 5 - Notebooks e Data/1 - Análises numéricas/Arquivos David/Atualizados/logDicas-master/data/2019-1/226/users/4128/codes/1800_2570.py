from numpy import*

x = array(eval(input("digite o x:")))
f = 1
m = sum(x)/size(x)
n = size(x)

for i in range(size(x)):
	f = abs(x[i] - m) * f
p = f**(1/n)
print(round(p,3))
	





