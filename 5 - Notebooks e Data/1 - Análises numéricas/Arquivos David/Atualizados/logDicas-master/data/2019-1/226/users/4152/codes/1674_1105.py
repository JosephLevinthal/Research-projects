# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
x = input("Digite aqui a descricao do brasao da casa: ").lower()

print("Entrada: ", x)

if (x == "lobo"):
	casa = "Casa: Stark"
elif (x == "leao"):
	casa = "Casa: Lannister"
elif (x == "veado"):
	casa = "Casa: Baratheon"
elif (x == "dragao"):
	casa = "Casa: Targaryen"
elif (x == "rosa"):
	casa = "Casa: Tyrell"
elif (x == "sol"):
	casa = "Casa: Martell"
elif (x == "lula"):
	casa = "Casa: Greyjoy"
elif (x == "esfolado"):
	casa = "Casa: Bolton"
elif (x == "turta"):
	casa = "Casa: Tully"
else:
	casa = "Brasao invalido"

print(casa)