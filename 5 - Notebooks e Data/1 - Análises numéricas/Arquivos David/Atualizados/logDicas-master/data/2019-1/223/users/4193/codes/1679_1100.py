# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
#leia o valor de uma celula

var = int(input("Digite o nome do animal:" ))

print("Entrada:",var)
if(var == 2):
	animal = "Tartaruga"
elif (var == 5):
	animal = "Garca"
elif (var == 10):
	animal = "Arara"
elif (var == 20):
	animal = "Mico-leao-dourado"
elif (var == 50):
	animal = "Onca pintada"
elif (var == 100):
	animal = "Garoupa"
else:
	animal = "Invalido"
print("Animal:",animal)
