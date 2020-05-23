# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a = input("Entrada:")
print('Entrada:', a)
if(a=="lobo"):
	b = "Casa: Stark"
elif(a=="leao"):
	b = "Casa: Lannister"
elif(a=="veado"):
	b = "Casa: Baratheon"
elif(a=="dragao"):
	b = "Casa: Targaryen"
elif(a=="rosa"):
	b = "Casa: Tyrell"
elif(a=="sol"):
	b = "Casa: Martell"
elif(a=="lula"):
	b = "Casa: Greyjoy"
elif(a=="esfolado"):
	b = "Casa: Bolton"	
elif(a=="turta"):
	b = "Casa: Tully"
else:
	b = "Brasao invalido"	
print(b)