from math import *
from numpy import *
from numpy.linalg import *
n = array(eval(input("Digite as notas dos estudantes: ")))
for i in range(shape(n)[0]):
	n[i,:] = sorted(n[i,:])
	media = mean(n[:,0])
print(round(media, 2))	

