from numpy import*
x = array(eval(input("digiti um vetor de numeros reais:")))
q = size(x)
m = sum(x)/q
p = 1
for i in range(size(x)):
	p = abs(x[i]-m)*p
p = p**(1/q)
print(round(p, 3))