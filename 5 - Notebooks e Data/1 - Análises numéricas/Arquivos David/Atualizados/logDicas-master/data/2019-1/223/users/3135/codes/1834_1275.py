from numpy import*
from numpy.linalg import*

ent= array(eval(input("AAAa:")))

horas= shape(ent)[0]
total= zeros(horas, dtype=int)			 
		 
for i in range(horas):
	total[i]= sum(ent[i,:])
print(total)
