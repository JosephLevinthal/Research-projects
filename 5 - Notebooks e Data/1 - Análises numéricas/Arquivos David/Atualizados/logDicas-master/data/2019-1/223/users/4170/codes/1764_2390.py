from numpy import*
p = array(eval(input("Quantidade de presentes por mes: ")))
f = array(eval(input("Quantidade de faltantes por mes: ")))
frequencia = p - f
maximo = max(frequencia)
if(maximo == frequencia[0]):
	print(1)
elif(maximo == frequencia[1]):
	print(2)
elif(maximo == frequencia[2]):
	print(3)	
elif(maximo == frequencia[3]):
	print(4)
elif(maximo == frequencia[5]):
	print(6)
elif(maximo == frequencia[6]):
	print(7)
elif(maximo == frequencia[7]):
	print(8)	
elif(maximo == frequencia[8]):
	print(9)
elif(maximo == frequencia[9]):
	print(10)
elif(maximo == frequencia[10]):
	print(11)
elif(maximo == frequencia[11]):
	print(12)	