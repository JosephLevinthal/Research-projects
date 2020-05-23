from numpy import *
x = array(eval(input("Insira os valores: ")))
m = sum(x) / size(x)
raiz = 1/size(x)
p = 1
for i in range(size(x)):
	p = p * abs(x[i] - m)
p = p**raiz
print(round(p,3))
	