from numpy import *
n = array(eval(input("Vetor: ")))
m = sum(n)/size(n)
soma = 0

for x in n:
	soma = soma + ((x - m)**2)
	
d = (soma/(size(n) - 1))**(1/2)	

print(round(d, 3))