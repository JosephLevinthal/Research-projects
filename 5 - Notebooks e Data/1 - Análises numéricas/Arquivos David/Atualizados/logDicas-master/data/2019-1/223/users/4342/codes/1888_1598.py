from numpy import *
from numpy.linalg import *

vet = array(eval(input("custo dos itens:")))

for i in range (size(vet)):
	if(vet[i] > 80):
		vet[i]= (vet[i] - 5)
X=sum(vet)
print(round(X, 2))