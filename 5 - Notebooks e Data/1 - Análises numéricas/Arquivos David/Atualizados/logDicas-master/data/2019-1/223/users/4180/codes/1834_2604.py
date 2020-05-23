from numpy import *
from numpy.linalg import *

pagamento = array(eval(input(":")))

for i in range(shape(pagamento)[0]):
	for j in range(7):
		if(pagamento[i,j] == max(pagamento[i,:])):
			print(pagamento[i,j])