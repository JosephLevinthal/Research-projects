# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
x = int(input("cedula: (2/5/10/20/50/100): "))

print("Entrada:", x)

if x == 2:
	animal = "Tartaruga"
elif x == 5:
	animal = "Garça"
elif x == 10:
	animal = "Arara"
elif x == 20:
	animal = "Mico-leao-dourado"
elif x == 50:
	animal = "Onca-pintada"
elif x == 100:
	animal = "Garoupa"
else:
	animal = "Invalido"

print("Animal:", animal)