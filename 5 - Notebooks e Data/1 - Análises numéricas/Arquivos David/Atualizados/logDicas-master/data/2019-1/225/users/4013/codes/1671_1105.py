# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
d = input("descricao da casa:")
print("Entrada:" , d)
if ((d != "lobo") and (d != "leao") and (d != "veado") and (d != "dragao") and (d != "rosa")
	 and (d != "sol") and (d != "lula") and (d != "esfolado") and (d != "turta")):
	print("Brasao invalido")
elif (d == "lobo"):
	print("Casa: Strak")
elif (d == "leao"):
	print("Casa: Lannister")
elif (d == "veado"):
	print("Casa: Baratheon")
elif (d == "dragao"):
	print("Casa: Targaryen")
elif (d == "rosa"):
	print("Casa: Tyrell")
elif (d == "sol"):
	print("Casa: Martell")
elif (d == "lula"):
	print("Casa: Greyjoy")
elif (d == "esfolado"):
	print("Casa: Bolton")
elif (d == "turta"):
	print("Casa: Tully")