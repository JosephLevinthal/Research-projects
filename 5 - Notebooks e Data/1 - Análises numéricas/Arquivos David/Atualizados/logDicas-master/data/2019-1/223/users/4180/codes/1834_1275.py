from numpy import *
from numpy.linalg import *

horas = array(eval(input("Horas por funcionarios: ")))
horas_total = zeros(shape(horas)[0],dtype=int)

for i in range(shape(horas)[0]):
	horas_total[i] = sum(horas[i,:])
print(horas_total)