from numpy import*

preco = array(eval(input("Custo dos itens: ")))

i = 0
desc = 0
total = sum(preco)

while(i < size(preco)):
	
	if(preco[i] > 80):
		desc = desc + 5
	else:
		desc = desc + 0
		
	i = i + 1
	
total = total - desc
print(round(total, 2))