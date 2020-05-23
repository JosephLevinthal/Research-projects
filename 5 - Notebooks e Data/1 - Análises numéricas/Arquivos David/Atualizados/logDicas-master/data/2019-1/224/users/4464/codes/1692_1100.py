# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
ceduula = int(input("valor da cedula: "))
print("Entrada:", ceduula)
if (ceduula == 5 or 2 or 10 or 20 or 50 or 100):
	if (ceduula == 2):
		mensagem = "Tartaruga"
		print("Animal:" , mensagem)
	elif (ceduula == 5):
		mensagem = "Garca"
		print("Animal:" , mensagem)
	elif (ceduula == 10):
		mensagem = "Arara"
		print("Animal:" , mensagem)
	elif (ceduula == 20):
		mensagem = "Mico-leao-dourado"
		print("Animal:" , mensagem)
	elif (ceduula == 50):
		mensagem = "Onca-pintada"
		print("Animal:" , mensagem)
	elif (ceduula == 100):
		mensagem = "Garoupa"
		print("Animal:" , mensagem)
	else:
		print("Animal: Invalido")
else:
	print("Animal: Invalido")
