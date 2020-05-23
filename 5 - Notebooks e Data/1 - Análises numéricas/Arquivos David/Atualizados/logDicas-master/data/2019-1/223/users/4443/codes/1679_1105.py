# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída

#leitura do brasao
bra = input("digite o nome do brasao: ")
bra = bra.lower()
print("Entrada: ", bra)

if (bra == "lobo"):
	print("Casa: Stark")
elif (bra == "leao"):
	print("Casa: Lannister")
elif (bra == "veado"):
	print("Casa: Baratheon")
elif (bra == "dragao"):
	print("Casa: Targaryen")	
elif (bra == "rosa"):
	print("Casa: Tyrell")
elif (bra == "sol"):
	print("Casa: Martell")	
elif (bra == "lula"):
	print("Casa: Greyjoy")	
elif (bra == "esfolado"):
	print("Casa: Bolton")	
elif (bra == "turta"):
	print("Casa: Tully")	
else:
	print("Brasao invalido")