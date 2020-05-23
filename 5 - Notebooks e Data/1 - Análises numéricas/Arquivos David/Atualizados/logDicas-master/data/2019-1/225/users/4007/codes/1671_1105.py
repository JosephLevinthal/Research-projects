# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
x = input("brasao:(lobo/leao/viado/dragao/rosa/sol/lula/esfolado/turta)")

if (x == "lobo"):
	y = "Stark"
	print("Entrada: ", x)
	print("Casa: ", y)
elif (x == "leao"):
	y = "Lannister"
	print("Entrada: ", x)
	print("Casa: ", y)
elif (x == "viado"):
	y = "Baratheon"
	print("Entrada: ", x)
	print("Casa: ", y)
elif (x == "dragao"):
	y = "Targaryen"
	print("Entrada: ", x)
	print("Casa: ", y)
elif (x == "rosa"):
	y = "Tyrell"
	print("Entrada: ", x)
	print("Casa: ", y)
elif (x == "sol"):
	y = "Martell"
	print("Entrada: ", x)
	print("Casa: ", y)
elif (x == "lula"):
	y = "Greyjoy"
	print("Entrada: ", x)
	print("Casa: ", y)
elif (x == "esfolado"):
	y = "Bolton"
	print("Entrada: ", x)
	print("Casa: ", y)
elif (x == "turta"):
	y = "Tully"
	print("Entrada: ", x)
	print("Casa: ", y)
else:
	print("Entrada: ", x)
	print("Brasao invalido")