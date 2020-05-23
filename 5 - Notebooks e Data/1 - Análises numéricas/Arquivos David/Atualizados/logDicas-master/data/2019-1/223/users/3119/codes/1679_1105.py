# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída

brasao = input("Digite o valor da cedula: ")

if(brasao == "lobo"):
	casa = "Casa: Stark"
elif(brasao == "leao"):
	casa = "Casa: Lannister"
elif(brasao == "veado"):
	casa = "Casa: Baratheon"
elif(brasao == "dragao"):
	casa = "Casa: Targaryen"
elif(brasao == "rosa"):
	casa = "Casa: Tyrell"
elif(brasao == "sol"):
	casa = "Casa: Martell"
elif(brasao == "lula"):
	casa = "Casa: Greyjoy"
elif(brasao == "esfolado"):
	casa = "Casa: Bolton"
elif(brasao == "turta"):
	casa = "Casa: Tully"
else:
	casa = "Brasao invalido"

print("Entrada:", brasao)
print(casa)