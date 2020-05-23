from numpy import *

preco = array(eval(input("custo: ")))


if(preco.any() > 80):
	x = sum(preco) - 5
	print(round(x,2))
else:
	y = sum(preco)
	print(round(y,2))