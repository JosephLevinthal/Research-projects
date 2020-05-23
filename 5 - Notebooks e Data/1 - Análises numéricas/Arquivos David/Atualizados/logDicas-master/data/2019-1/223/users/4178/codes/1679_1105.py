# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
x = input("Sua casa: ").lower()

if (x == "lobo"):
	msg = "Stark"
elif (x == "leao"):
	msg = "Lennister"
elif (x == "veado"):
	msg = "Baratheon"
elif (x == "dragao"):
	msg = "Targaryen"
elif (x == "rosa"):
	msg = "Tyrell"
elif (x == "sol"):
	msg = "Martell"
elif (x == "lula"):
	msg = "Greyjoy"
elif (x == "esfolado"):
	msg = "Bolton"
elif (x == "turta"):
	msg = "Tully"
else:
	msg = "Brasao invalido"
print ("Entrada: ", x)
print ("Casa: ",msg)

