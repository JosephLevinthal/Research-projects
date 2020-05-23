# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
x= input("Qual o brasao? ").lower()

print("Entrada:",x)

if(x=="lobo"):
	y= "Casa: Stark"
elif (x=="leao"):
	y= "Casa: Lannister"
elif (x=="veado"):
	y= "Casa: Baratheon"
elif (x=="dragao"):
	y= "Casa: Targaryen"
elif (x=="rosa"):
	y= "Casa: Tyrell"
elif (x=="sol"):
	y= "Casa: Martell"
elif (x=="lula"):
	y= "Casa: Greyjoy"
elif (x=="esfolado"):
	y= "Casa: Bolton"
elif (x=="turta"):
	y= "Casa: Tully"
else:
	y= "Brasao invalido"
	
print(y)

