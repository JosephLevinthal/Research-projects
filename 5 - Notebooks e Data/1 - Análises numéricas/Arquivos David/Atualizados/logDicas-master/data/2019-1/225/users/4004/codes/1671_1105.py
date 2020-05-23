# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
x = input("descricao do brasao: ")

print("Entrada: ", x)

if x.lower() == "lobo":
	y = "Stark"
elif x.lower() == "leao":
	y = "Lannister"
elif x.lower() == "veado":
	y = "Baratheon"
elif x.lower() == "dragao":
	y = "Targaryen"
elif x.lower() == "rosa":
	y = "Tyrell"
elif x.lower() == "sol":
	y = "Martell"
elif x.lower() == "lula":
	y = "Greyjoy"
elif x.lower() == "esfolado":
	y = "Bolton"
elif x.lower() == "turta":
	y = "Tully"
else:
	y = "Brasao invalido"

if y == "Brasao invalido":
	print(y)
else:
	print("Casa: ",y)