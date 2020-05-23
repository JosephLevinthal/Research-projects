from numpy import *
v = array(eval(input("Custo dos itens: ")))

t = 0

total = sum(v)

while (t < size(v)):
	if (v[t] > 80):
		total = total - 5
		
	t = t + 1
	
print(round(total, 2))

