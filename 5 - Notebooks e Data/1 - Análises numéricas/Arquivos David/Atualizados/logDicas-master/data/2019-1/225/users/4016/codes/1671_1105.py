# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
X=input("Descrico do brasao:").lower()
print("Entrada:",X)
if(X=="lobo"):
	print("Casa: Stark")
elif(X=="leao"):
	print("Casa: Lannister")
elif(X=="veado"):
	print("Casa: Baratheon")
elif(X=="dragao"):
	print("Casa: Targaryen")
elif(X=="rosa"):
	print("Casa: Tyrell")
elif(X=="sol"):
	print("Casa: Martell")
elif(X=="lula"):
	print("Casa: Greyjoy")
elif(X=="esfolado"):
	print("Casa: Bolton")
elif(X=="turta"):
	print("Casa: Tully")
else:
	print("Brasao invalido")