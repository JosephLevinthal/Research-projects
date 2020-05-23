# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída

brasao = input("Descricao do brasao: ").lower()
print('Entrada:', brasao)

if (brasao == 'lobo'):
	print("Casa: Stark")
elif (brasao == 'leao'):
	print("Casa: Lannister")
elif (brasao == 'veado'):
	print("Casa: Baratheon")
elif (brasao == 'dragao'):
	print("Casa: Targaryen")
elif (brasao == 'rosa'):
	print("Casa: Tyrell")
elif (brasao == 'sol'):
	print("Casa: Martell")
elif (brasao == "lula"):
	print("Casa: Greyjoy")
elif (brasao == "esfolado"):
	print("Casa: Bolton")
elif (brasao == "turta"):
	print("Casa: Tully")
else:
	print("Brasao invalido")