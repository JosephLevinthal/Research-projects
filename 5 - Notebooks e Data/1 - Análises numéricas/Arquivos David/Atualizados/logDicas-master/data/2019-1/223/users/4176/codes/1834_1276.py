from numpy import *
from numpy.linalg import *

horas = array(eval(input('Digite: ')))
horas_dia = zeros(7,dtype=int)

for j in range(7):
	horas_dia[j] = sum(horas[:,j])
for j in range(7):
	if(horas_dia[j] == max(horas_dia)):
		print(j+1)