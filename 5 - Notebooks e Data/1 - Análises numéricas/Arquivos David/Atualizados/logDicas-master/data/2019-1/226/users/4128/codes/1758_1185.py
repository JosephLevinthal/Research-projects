from numpy import*

pg = array(eval(input("Glicose do paciente:")))
i = 0
s = 0
while(i != size(pg)):
	if(pg[i] > 99):
		print(i)
		s = s+ 1
	i = i + 1
print(s)