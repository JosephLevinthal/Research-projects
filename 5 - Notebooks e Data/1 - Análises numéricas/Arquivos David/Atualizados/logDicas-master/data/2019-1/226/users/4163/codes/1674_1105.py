# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = input("digite o brasao: ").lower()
print("Entrada:",a)

if (a == "lobo"):
	print("Casa: Stark")	
elif (a == "leao"):
	print("Casa: Lannister")
elif (a == "veado"):
	print("Casa: Baratheon")
elif (a == "rosa"):
	print("Casa: tyrell")
elif (a == "sol"):
	print("Casa: Martell")
elif (a == "lula"):
	print("Casa: Greyjoy")
elif (a == "esfolado"):
	print("Casa: Bolton")
elif (a == "turta"):
	print("Casa: Tully")
elif (a == "dragao"):
	print("Casa: Targaryen")
else:
	print(("Brasao invalido"))
