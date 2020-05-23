# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
v=int(input("Qua o valor da cedula?: "))
if (v==2 or v==5 or v==10 or v==20 or v==50 or v==100):
	if (v==2):
		print("Entrada:", v)
		print("Animal: Tartaruga")
	if (v==5):
		print("Entrada:", v)
		print("Animal: Garca")
	if (v==10):
		print("Entrada:", v)
		print("Animal: Arara")
	if (v==20):
		print("Entrada:", v)
		print("Animal: Mico-leao-dourado")
	if (v==50):
		print("Entrada:", v)
		print("Animal: Onca-pintada")
	if (v==100):
		print("Entrada:", v)
		print("Animal: Garoupa")
else:
	print("Entrada:", v)
	print("Animal: Invalido")