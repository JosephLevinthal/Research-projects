a = float(input('Digite o coeficiente a: '))
b = float(input('Digite o coeficiente b: '))
c = float(input('Digite o coeficiente c: '))
d = float(input('Digite o coeficiente d: '))
e = float(input('Digite o coeficiente e: '))
f = float(input('Digite o coeficiente f: '))

if (a*e-b*d)==0:
	print('Nao tem solucao')
	
else:
	print((c*e-b*f)/(a*e-b*d))
	print((a*f-c*d)/(a*e-b*d))