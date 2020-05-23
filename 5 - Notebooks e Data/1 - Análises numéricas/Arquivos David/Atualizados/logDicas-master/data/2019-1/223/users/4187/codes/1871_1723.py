from numpy import*
from numpy.linalg import*
produtos = array(eval(input("quantidades e precos: ")))

preco = 0
for i in range(shape(produtos)[0]): 
	preco = preco + produtos[i,0] * produtos[i,1]
print(round(preco,2))