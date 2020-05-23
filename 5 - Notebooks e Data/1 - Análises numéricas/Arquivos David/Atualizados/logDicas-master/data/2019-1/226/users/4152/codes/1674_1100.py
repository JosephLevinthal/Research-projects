# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
ced = int(input("digite o valor da cedula: "))
a = "Tartaruga"
b = "Garca"
c = "Arara"
d = "Mico-leao-dourado"
e = "Onca-pintada"
f = "Garoupa"
if ((ced == 2) or (ced == 5) or (ced == 10) or (ced == 20) or (ced == 50) or (ced == 100)):
	if (ced == 2):
		print("Entrada:", ced)
		print("Animal:", a)
	elif (ced == 5):
		print("Entrada:", ced)
		print("Animal:", b)
	elif (ced == 10):
		print("Entrada:", ced)
		print("Animal:", c)
	elif (ced == 20):
		print("Entrada:", ced)
		print("Animal:", d)
	elif (ced == 50):
		print("Entrada:", ced)
		print("Animal:", e)
	else:
		print("Entrada:", ced)
		print("Animal:", f)
else:
	print("Entrada:", ced)
	print("Animal:", "Invalido")
		