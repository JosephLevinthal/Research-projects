from numpy import*
faltas = array(eval(input("Digite: ")))
soma = size(faltas)

faltas2= 0
faltas3= 0
faltas4= 0
faltas5= 0
faltas6= 0
faltas7= 0

for i in range(size(faltas)):
	
	if(faltas[i] == 2):
		faltas2 = faltas2 + 1
	elif(faltas[i] == 3):
		faltas3 = faltas3 + 1
	elif(faltas[i] == 4):
		faltas4 = faltas4 + 1
	elif(faltas[i] == 5):
		faltas5 = faltas5 + 1
	elif(faltas[i] == 6):
		faltas6 = faltas6 + 1
	elif(faltas[i] == 7):
		faltas7 = faltas7 + 1
	p2 = (100 * faltas2)/soma
	p3 = (100 * faltas3)/soma
	p4 = (100 * faltas4)/soma
	p5 = (100 * faltas5)/soma
	p6 = (100 * faltas6)/soma
	p7 = (100 * faltas7)/soma
if( 2 <= faltas[i] <= 7):
	z = zeros(6, dtype=float)
	z[0] = round(p2,1)
	z[1] = round(p3,1)
	z[2] = round(p4,1)
	z[3] = round(p5,1)
	z[4] = round(p6,1)
	z[5] = round(p7,1)
	print(z) 