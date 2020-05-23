from numpy import *
x = array(eval(input("Vetor: ")))
n = size(x)
m = sum(x)/size(x)
aux = 0
for i in range(size(x)):
	aux = aux + (x[i] - m) ** 2
d = (aux / (n - 1)) ** (1/2)
print(round(d, 3))
