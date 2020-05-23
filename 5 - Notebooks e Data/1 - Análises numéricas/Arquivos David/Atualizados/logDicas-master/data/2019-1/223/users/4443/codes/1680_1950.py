#Coleta dos dados de temperatura e velocidade do vento
tar = float(input("Digite o valor da temperatura em Celcius(C): "))
v = float(input("Digite a velocidade do vento: "))

#verificacao dos valores de temperatura e velocidade
if(tar < -50) or (tar > 10):
	print("Temperatura invalida")
elif(v <= 4.8):
	print("Velocidade invalida")
else:
	s = 13.12+(0.6215*tar)-(11.37*v**0.16)+(0.3965*tar*v**0.16)
	print(round(s, 4))
