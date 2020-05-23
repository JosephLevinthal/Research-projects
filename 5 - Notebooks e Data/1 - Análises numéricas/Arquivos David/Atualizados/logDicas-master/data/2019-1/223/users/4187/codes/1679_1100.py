# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
valor = int(input("valor da cedula: "))

if(valor != 2 and valor != 5 and valor != 10 and valor != 20 and valor != 50 and valor != 100 ):
	print("Entrada:",valor)
	print("Animal:","Invalido")

elif( valor == 2):
	print("Entrada:",valor)
	print("Animal:","Tartaruga")
elif(valor == 5):
	print("Entrada:",valor)
	print("Animal:","Garca")
elif(valor == 10):
	print("Entrada:",valor)
	print("Animal:","Arara")
elif(valor == 20):
	print("Entrada:",valor)
	print("Animal:","Mico-leao-dourado")
elif(valor == 50):
	print("Entrada:",valor)
	print("Animal:","Onca-pintada")
elif(valor == 100):
	print("Entrada:",valor)
	print("Animal:","Garoupa")
	

