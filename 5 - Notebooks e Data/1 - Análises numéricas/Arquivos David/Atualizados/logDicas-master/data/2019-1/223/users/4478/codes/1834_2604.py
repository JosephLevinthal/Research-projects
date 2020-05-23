from numpy import*
from numpy.linalg import*

func = array(eval(input("horas trabalhadas")))

for i in range(shape(func)[0]):
	print(max(func[i,:]))