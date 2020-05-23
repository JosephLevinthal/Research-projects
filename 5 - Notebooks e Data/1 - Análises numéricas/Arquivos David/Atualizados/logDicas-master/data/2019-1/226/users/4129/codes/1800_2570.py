from numpy import*

x = array(eval(input("Vetor:")))
n = size(x)
m = sum(x)/n
p = 1
for i in range(size(x)):
	p = abs(x[i]-m)*p
p = p**(1/n)
print(round(p, 3))