from numpy import*
NG = array(eval(input("Nivel de Glicose dos pacientes em 99mg/dl:")))
i = 0
n = 0
while(i < size(NG)):
	if(NG[i] > 99 ):
		print(i)
		n = n + 1
	i = i + 1
print(n)
