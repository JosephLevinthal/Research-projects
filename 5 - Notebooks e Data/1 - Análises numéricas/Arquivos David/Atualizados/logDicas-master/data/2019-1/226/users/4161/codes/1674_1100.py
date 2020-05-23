# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
x = int(input("nota: "))
y = "Invalido"
if x == 2:
	y = "Tartaruga"
if x == 5:
	y = "Garca"
if x == 10:
	y = "Arara"
if x == 20:
	y = "Mico-leao-dourado"
if x == 50:
	y = "Onca-pintada"
if x ==100:
	y = "Garoupa"
print("Entrada:", x)
print("Animal:", y)