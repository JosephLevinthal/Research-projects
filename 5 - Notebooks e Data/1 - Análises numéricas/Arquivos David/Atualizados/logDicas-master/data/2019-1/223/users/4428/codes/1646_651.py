altura = float(input("Digite a altura: "))
sexo = input("Digite o sexo: ")

if(sexo == M):
	ideal = ((72.7*altura) - 58)

else:
	ideal = ((62.1*altura) - 44.7)
	
print (round(ideal, 2))