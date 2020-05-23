from numpy import*

nivelGlicose = array(eval(input("Nivel de Glicose no sangue: ")))
							
i = 0
n = 0
							
while(i < size(nivelGlicose)):
	if(nivelGlicose[i] > 99 ):
		print(i)
		n = n + 1
	i = i + 1
							
print(n)