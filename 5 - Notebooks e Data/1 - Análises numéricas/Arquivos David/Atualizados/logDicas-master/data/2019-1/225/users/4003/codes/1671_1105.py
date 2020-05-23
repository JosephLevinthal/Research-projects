# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída

X = input("x")

print("Entrada:", X)

if (X == "lobo"):
	Casa = "Stark"
	print("Casa: ", Casa)
elif (X == "leao"):
	Casa = "Lannister"
	print("Casa: ", Casa)
elif (X == "veado"):
	Casa = "Baratheon"
	print("Casa: ", Casa)
elif (X == "dragao"):
	Casa = "Targaryen"
	print("Casa: ", Casa)
elif (X == "rosa"):
	Casa = "Tyrell"
	print("Casa: ", Casa)
elif (X == "sol"):
	Casa = "Martel"
	print("Casa: ", Casa)
elif (X == "lula"):
	Casa = "Greyjoy"
	print("Casa: ", Casa)
elif (X == "esfolado"):
	Casa = "Bolton"
	print("Casa: ", Casa)
elif (X == "turta"):
	Casa = "Tully"
	print("Casa: ", Casa)
else:
	Casa = "Brasao invalido"
	print(Casa)