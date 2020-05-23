# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a=input("digite o nome: ")
print("Entrada:",a)
if(a.lower()=="lobo"):
	print("Casa: Stark")
elif (a.lower()=="leao"):
	print("Casa: Lannister")
elif (a.lower()=="veado"):
	print("Casa: Baratheon")
elif (a.lower()=="dragao"):
	print("Casa: Targaryen")
elif (a.lower()=="rosa"):
	print("Casa: Tyrell")
elif (a.lower()=="sol"):
	print("Casa: Martell")
elif (a.lower()=="lula"):
	print("Casa: Greyjoy")
elif (a.lower()=="esfolado"):
	print("Casa: Bolton")
elif (a.lower()=="turta"):
	print("Casa: Tully")
else:
	print("Brasao invalido")