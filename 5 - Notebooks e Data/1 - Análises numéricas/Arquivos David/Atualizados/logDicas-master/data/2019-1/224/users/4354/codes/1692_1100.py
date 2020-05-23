# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
entrada = int(input("valor da cedula: "))

if(entrada == 2):
	print("Entrada:",entrada)
	print("Animal:","Tartaruga")
elif(entrada == 5):
	print("Entrada:",entrada)
	print("Animal:","Garca")
elif(entrada == 10):
	print("Entrada:",entrada)
	print("Animal:","Arara")
elif(entrada == 20):
	print("Entrada:",entrada)
	print("Animal:","Mico-leao-dourado")
elif(entrada == 50):
	print("Entrada:",entrada)
	print("Animal:","Onca-pintada")
elif(entrada == 100):
	print("Entrada:",entrada)
	print("Animal:","Garoupa")	
else:
	print("Entrada:",entrada)
	print("Animal:","Invalido")