from numpy import *
n = array(eval(input("Vetor: ")))
m = sum(n)/size(n)
soma = 1

for x in n:
	soma = soma*(abs(x - m))
	
p = (soma)**(1/size(n))

print(round(p, 3))