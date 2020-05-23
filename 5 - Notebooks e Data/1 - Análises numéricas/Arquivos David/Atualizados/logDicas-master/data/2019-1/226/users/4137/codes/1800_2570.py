from numpy import*

x = array(eval(input("Insira um numero real:")))

p = 1
m = sum(x)/size(x)
n = size(x)

for i in range(size(x)):
	p = abs(p*(x[i]-m))
p = p**(1/n)
print(round(p,3))