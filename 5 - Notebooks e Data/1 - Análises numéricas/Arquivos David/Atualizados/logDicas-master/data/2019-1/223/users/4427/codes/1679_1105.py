# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída

x= input ("descricao do brasao:  ")
print ("Entrada:",x)

if (x !="lobo" and x !="leao" and x !="veado" and x !="dragao" and x !="rosa" and x !="sol" and x !="lula" and x !="esfolado" and x !="turta"):
	print ("Brasao invalido")
elif (x=="lobo"):
	print ("Casa: Stark")
elif (x=="leao"):
	print ("Casa: Lannister")
elif (x=="veado"):
	print ("Casa: Baratheon")
elif (x=="dragao"):
	print ("Casa: Targaryen")
elif (x=="rosa"):
	print ("Casa: Tyrell")
elif (x=="sol"):
	print ("Casa: Martell")
elif (x=="lula"):
	print ("Casa: Greyjoy")
elif (x=="esfolado"):
	print ("Casa: Bolton")
elif (x=="turta"):
	print ("Casa: Tully")