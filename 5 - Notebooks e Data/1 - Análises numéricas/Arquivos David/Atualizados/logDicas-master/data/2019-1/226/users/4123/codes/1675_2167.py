# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
dest = input()
per = input()
x = 0
x = 650 if dest == "Belem" else x
x = 152 if dest == "Borba" else x
x = 199 if dest == "Coari" else x
x = 390 if dest == "Humaita" else x
x = 280 if dest == "Manicore" else x
x = 190 if dest == "Maues" else x

if per == "ida":
	x = 350 if x == 650 else x
	x = 80 if x == 152 else x
	x = 106 if x == 199 else x
	x = 200 if x == 390 else x
	x = 150 if x == 280 else x
	x = 100 if x == 190 else x

if x == 0:
	print("Destino inexistente")
else:
	print(x)