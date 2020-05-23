# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
X = int(input("digite o valor da cedula: "))

if X == 2 :
	Y = "Tartaruga"
	print("Entrada: ", X)
	print("Animal: ", Y)
elif X == 5:
	Y = "Garca"
	print("Entrada: ", X)
	print("Animal: ", Y)
elif X == 10 :
	Y = "Arara"
	print("Entrada: ", X)
	print("Animal: ", Y)
elif X == 20 :
	Y = "Mico-leao-dourado"
	print("Entrada: ", X)
	print("Animal: ", Y)
elif X == 50 :
	Y = "Onca-pintada"
	print("Entrada: ", X)
	print("Animal: ", Y)
elif (X == 100) :
	Y = "Garoupa"
	print("Entrada: ", X)
	print("Animal: ", Y)
else :
	Y = "Invalido"
	print("Entrada: ", X)
	print("Animal:", Y)
