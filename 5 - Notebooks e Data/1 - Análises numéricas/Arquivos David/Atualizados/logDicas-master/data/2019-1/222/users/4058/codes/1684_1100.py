# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.

cedula= int(input("valor da cedula:"))
print("Entrada:", cedula)
if (cedula!=2 and cedula!=5 and cedula!=10 and cedula!=20 and cedula!=50 and cedula!=100):
	print("Animal: Invalido")
else:
	if (cedula==2):
		animal= "Tartaruga"
		print("Animal:", animal)
	elif (cedula==5):
		animal= "Garca"
		print("Animal:", animal)
	elif (cedula==10):
		animal= "Arara"
		print("Animal:", animal)
	elif (cedula==20):
		animal= "Mico-leao-dourado"
		print("Animal:", animal)
	elif (cedula==50):
		animal= "Onca-pintada"
		print("Animal:", animal)
	elif (cedula==100):
		animal= "Garoupa"
		print("Animal:", animal)
	