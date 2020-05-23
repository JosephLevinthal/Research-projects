from numpy import *
from numpy.linalg import *

pagamento = array(eval(input("Matriz: ")))

for i in range(shape(pagamento)[0]):
	print(max(pagamento[i,:]))