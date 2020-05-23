from numpy import *
vg= array(eval(input("digite o nivel de glicose dos pacientes: ")))
i=0
d=0
while(i<len(vg)):
	if(vg[i]>99):
		print(i)
		d=d+1
	i=i+1
print(d)
