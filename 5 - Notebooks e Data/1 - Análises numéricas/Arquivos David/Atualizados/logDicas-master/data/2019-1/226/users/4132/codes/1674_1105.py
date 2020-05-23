# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída

descricao=input("Digite o brasao: ").lower()

print("Entrada: ",descricao)

if(descricao=="lobo"):
	print("Casa: Stark")
elif(descricao == "leao"):
	print("Casa: Lannister")
elif(descricao=="veado"):
	print("Casa: Baratheon")
elif(descricao=="dragao"):
	print("Casa: Targaryen")
elif(descricao=="rosa"):
	print("Casa: Tyrell")
elif(descricao=="sol"):
	print("Casa: Martell")
elif(descricao=="lula"):
	print("Casa: Greyjoy")
elif(descricao=="esfolado"):
	print("Casa: Bolton")
elif(descricao=="turta"):
	print("Casa: Tully")
else:
	print("Brasao invalido")
