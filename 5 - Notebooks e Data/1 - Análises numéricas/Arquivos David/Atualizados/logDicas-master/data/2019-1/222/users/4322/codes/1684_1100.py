# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a = int(input("qual o valor da nota? "))
if(a == 2):
	print("Entrada: ", a)
	print("Animal: Tartaruga")
elif(a == 5):
	print("Entrada: ", a)
	print("Animal:	Garça")
elif(a == 10):
	print("Entrada: ", a)
	print("Animal: Arara")
elif(a == 20):
	print("Entrada: ", a)
	print("Animal:	Mico-leao-dourado")
elif(a == 50):
	print("Entrada: ", a)
	print("Animal: Onca-pintada")
elif(a == 100):
	print("Entrada: ", a)
	print("Animal: Garoupa")
elif(a != 2) and (a != 5) and (a != 10) and (a != 20) and (a != 50) and (a != 100):
	print("Entrada: ", a)
	print("Animal: Invalido")
	