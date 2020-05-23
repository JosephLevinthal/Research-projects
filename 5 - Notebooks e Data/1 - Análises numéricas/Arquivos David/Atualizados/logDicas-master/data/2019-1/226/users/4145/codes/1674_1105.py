# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
x = input(" brasao: ").lower()
print("Entrada:", x)
if(x=="lobo"):
	y = "Stark"
	print("Casa:", y)
elif(x=="leao"):
	y = "Lannister"
	print("Casa:", y)
elif(x=="veado"):
	y = "Baratheon"
	print("Casa:", y)
elif(x=="dragao"):
	y = "Targaryen"
	print("Casa:", y)
elif(x=="rosa"):
	y = "Tyrell"
	print("Casa:", y)
elif(x=="sol"):
	y ="Martell"
	print("Casa:", y)
elif(x=="lula"):
	y = "Greyjoy"
	print("Casa:", y)
elif(x=="esfolado"):
	y = "Bolton"
	print("Casa:", y)
elif(x=="turta"):
	y = "Tully"
	print("Casa:", y)
else:
	y = "Brasao invalido"
	print(y)
#print("Casa:", y)
