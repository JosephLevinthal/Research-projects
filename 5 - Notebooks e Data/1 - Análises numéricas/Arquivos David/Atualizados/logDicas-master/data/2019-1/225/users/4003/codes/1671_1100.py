# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.

cedula = int(input("valor da cedula:"))

if (cedula == 2):
	animal = "Tartaruga"
elif (cedula == 5):
	animal = "Garca"
elif (cedula == 10):
	animal = "Arara"
elif (cedula == 20):
	animal = "Mico-leao-dourado"
elif (cedula == 50):
	animal = "Onca-pintada"
elif (cedula == 100):
	animal = "Garoupa"
else:
	animal = "Erro"

print("Entrada:", cedula)

if animal == "Erro":
	print("Animal: Invalido")
else:
	print("Animal:", animal)