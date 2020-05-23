from numpy import*
from numpy.linalg import*
i=0
ent= array(eval(input("AAAa:")))

horas= shape(ent)[1]
total= zeros(horas, dtype=int)			 
		 
for i in range(horas):
	total[i]= sum(ent[:,i])

for i in range(horas):
	if(total[i] >= max(total)):
		print(i+1)