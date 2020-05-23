from numpy import*
massa=array(eval(input("Massas: ")))#Massa
altura=array(eval(input("Alturas: ")))#Altura
v = zeros(size(massa), dtype=float)# IMC

for i in range(0, size(massa)):

	v[i]= round(massa[i]/(altura[i]**2), 2)

	if(v[i]<17):
		a="MUITO ABAIXO DO PESO"
	elif(v[i]>=17 and v[i]<=18.49):
		a="ABAIXO DO PESO"
	elif(v[i]>=18.5 and v[i]<=24.99):
		a="PESO NORMAL"
	elif(v[i]>=25 and v[i]<=29.99):
		a="ACIMA DO PESO"
	elif(v[i]>=30 and v[i]<=34.99):
		a="OBESIDADE"
	elif(v[i]>=35 and v[i]<=39.99):
		a="OBESIDADE SEVERA"
	else:
		a="OBESIDADE MORBIDA"
		
print(v)
print("O MAIOR IMC DA TURMA EH:",max(v))
print(a)