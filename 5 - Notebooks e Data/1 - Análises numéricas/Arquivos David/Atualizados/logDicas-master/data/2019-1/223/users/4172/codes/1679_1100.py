# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.

A=int(input("Entrada: "))

if (A==2)or(A==5)or(A==10)or(A==20)or(A==50)or(A==100):
	if (A==2):
		Y="Tartaruga"
	elif(A==5):
		Y="Garca"
	elif(A==10):
		Y="Arara"
	elif(A==20):
		Y="Mico-leao-dourado"
	elif(A==50):
		Y="Onca-pintada"
	elif(A==100):
		Y="Garoupa"
	print("Entrada:", A)
	print("Animal:", Y)
else:
	print("Entrada:", A)
	print("Animal: Invalido")

