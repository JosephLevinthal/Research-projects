# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
x = int(input("insira o valor da celula: "))
print("Entrada: ", x)
if (x == 2):
	Animal = "Tartaruga"
elif (x == 5):
	Animal = "Garça"
elif (x == 10):
	Animal = "Arara"
elif (x == 20):
	Animal = "Mico-leao-dourado"
elif (x == 50):
	Animal = "Onca-pintada"
elif (x == 100):
	Animal = "Garoupa"
else:
	Animal = "Invalido"

print("Animal: ", Animal)