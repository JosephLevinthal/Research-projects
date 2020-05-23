from numpy import*
massa = array(eval(input("massa:")))
altura = array(eval(input("altura:")))
imc = zeros(size(massa), dtype=float)

for i in range(size(massa)):
	imc[i] = massa[i] / (altura[i]**2)
	imc[i] = round(imc[i],2)
print(imc)				

maiorimc = max(imc)
print("O MAIOR IMC DA TURMA EH:", maiorimc)


if (maiorimc < 17):
	msg = "muito abaixo do peso"
elif(maiorimc >= 17 and maiorimc < 18.49):
	msg = "abaixo do peso"
elif(maiorimc >= 18.5 and maiorimc < 24.99):
	msg = "peso normal"
elif(maiorimc >= 25 and maiorimc < 29.99):
	msg = "acima do peso"
elif(maiorimc >= 30 and maiorimc < 34.99):
	msg = "obesidade"
elif(maiorimc >= 35 and maiorimc < 39.99):
	msg = "obesidade severa"
elif(maiorimc > 40):
	msg = "obesidade morbida"
print(msg.upper())	
	





