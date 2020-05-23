# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
desc = input("descricao do brasao: ")
print("Entrada:" , desc,)
if( desc == "lobo" ):
	print("Casa: Stark")
elif( desc == "leao" ):
	print("Casa: Lannister")
elif( desc == "veado" ):
	print( "Casa: Baratheon" )
elif( desc == "dragao" ):
	print("Casa: Targaryen")
elif( desc == "rosa"):
	print("Casa: Tyrell")
elif( desc == "sol"):
	print("Casa: Martell")
elif( desc == "lula"):
	print("Casa: Greyjoy")
elif( desc == "esfolado"):
	print("Casa: Bolton")
elif( desc == "turta"):
	print("Casa: Tully")
else:
	print("Brasao invalido")