from numpy import*

pres = array(eval(input("Digite o vetor dos presentes: ")))
fal = array(eval(input("Digite o vetor dos faltantes: ")))

f = pres - fal
maximo = max(f)
if(maximo == f[0]):
	print(1)
elif(maximo == f[1]):
	print(2)
elif(maximo == f[2]):
	print(3)
elif(maximo == f[3]):
	print(4)
elif(maximo == f[4]):
	print(5)
elif(maximo == f[5]):
	print(6)
elif(maximo == f[6]):
	print(7)
elif(maximo == f[7]):
	print(8)
elif(maximo == f[8]):
	print(9)
elif(maximo == f[9]):
	print(10)	
elif(maximo == f[10]):
	print(11)
elif(maximo == f[11]):
	print(12)