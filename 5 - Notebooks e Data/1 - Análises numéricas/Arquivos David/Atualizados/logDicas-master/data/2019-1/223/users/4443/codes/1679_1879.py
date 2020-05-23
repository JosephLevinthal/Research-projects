# Digite o numero de horas extras:
HE = float(input("Digite o numero de horas extras: "))
NT = float(input("Digite o numero de horas nao trabalhadas: "))

#Calculo do indice H:
H = HE - (0.25*NT)
print(HE, "extras e",NT, "de falta")

if(H > 400):
	print("R$", round(500.00, 2))
elif(H <= 400):
	print("R$", round(100.00, 2))
	
