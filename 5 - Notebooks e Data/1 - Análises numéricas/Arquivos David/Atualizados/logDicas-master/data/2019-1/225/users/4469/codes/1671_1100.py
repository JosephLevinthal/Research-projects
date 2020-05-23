# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
x = int(input())

print("Entrada: " + str(x))

if(x == 2 or x == 5 or x == 10 or x == 20 or x == 50 or x == 100):
	if(x == 2):
		print("Animal: Tartaruga")
	elif(x == 5):
		print("Animal: Garca")
	elif(x == 10):
		print("Animal: Arara")
	elif(x == 20):
		print("Animal: Mico-leao-dourado")
	elif(x == 50):
		print("Animal: Onca-pintada")
	else:
		print("Animal: Garoupa")
else:
	print("Animal: Invalido")