from numpy import*
custo = array(eval(input("custo dos itens:")))
i = 0
desconto = sum(custo)
while(size[0:-1]):
if(custo[i] >= 80):
	desconto = sum(custo) - 5 
	i = i + 1
print(round(desconto, 2))
