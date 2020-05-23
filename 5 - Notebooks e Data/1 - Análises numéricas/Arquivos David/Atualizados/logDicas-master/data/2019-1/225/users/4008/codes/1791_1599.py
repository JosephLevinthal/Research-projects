from numpy import *
preco = array(eval(input("custo: ")))
i = 0
p = 0
while(i < size(preco)):
	if(preco[i] > 80.0):
		p = p + preco[i]*(15/100) 
		i = i + 0
	else:
		p = p + preco[i]
		i = i + 1
print(round(sum(p), 2))