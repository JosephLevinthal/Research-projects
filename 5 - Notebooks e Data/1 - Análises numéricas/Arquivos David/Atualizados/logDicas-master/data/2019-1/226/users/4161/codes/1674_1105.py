# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
x = input("brasao: ")
print("Entrada:", x)
y = "Brasao invalido"
if x.lower() == "lobo":
	y = "Casa: Stark"
elif x.lower() == "leao":
	y = "Casa: Lannister"
elif x.lower() == "veado":
	y = "Casa: Baratheon"
elif x.lower() == "dragao":
	y = "Casa: Targaryen"
elif x.lower() == "rosa":
	y = "Casa: Tyrell"
elif x.lower() == "sol":
	y = "Casa: Martell"
elif x.lower() == "lula":
	y = "Casa: Greyjoy"
elif x.lower() == "esfolado":
	y = "Casa: Bolton"
elif x.lower() == "turta":
	y = "Casa: Tully"
print(y)
