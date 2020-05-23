# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
X=input()
print("Entrada:",X)
if(X=="lobo"):
	Y="Stark"
elif(X=="leao"):
	Y="Lannister"
elif(X=="veado"):
	Y="Baratheon"
elif(X=="dragao"):
	Y="Targaryen"
elif(X=="rosa"):
	Y="Tyrell"
elif(X=="sol"):
	Y="Martell"
elif(X=="lula"):
	Y="Greyjoy"
elif(X=="esfolado"):
	Y="Bolton"
elif(X=="turta"):
	Y="Tully"
else:
	Y="Brasao invalido"

if(Y!="Brasao invalido"):
	print("Casa:",Y)
else:
	print(Y)
