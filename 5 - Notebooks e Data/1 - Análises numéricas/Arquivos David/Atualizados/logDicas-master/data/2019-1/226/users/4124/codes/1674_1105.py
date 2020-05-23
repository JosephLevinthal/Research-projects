# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída

br = input("Brasao: ").lower()
if(br == "lobo"):
	x = "Casa: Stark"
elif(br == "leao"):
	x = "Casa: Lannister"
elif(br == "veado"):
	x = "Casa: Baratheon"
elif(br == "dragao"):
	x = "Casa: Targaryen"
elif(br == "rosa"):
	x = "Casa: Tyrell"
elif(br == "sol"):
	x = "Casa: Martell"
elif(br == "lula"):
	x = "Casa: Greyjoy"
elif(br == "esfolado"):
	x = "Casa: Bolton"
elif(br == "turta"):
	x = "Casa: Tully"
else:
	x = "Brasao invalido"
print("Entrada:", br,)
print(x)