# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
desc = input()
x = ""
x = "Stark" if desc == "lobo" and x ==""  else x
x = "Lannister" if desc == "leao" and x ==""  else x
x = "Baratheon" if desc == "veado" and x ==""  else x
x = "Targaryen" if desc == "dragao" and x ==""  else x
x = "Tyrell" if desc == "rosa" and x ==""  else x
x = "Martell" if desc == "sol" and x =="" else x
x = "Greyjoy" if desc == "lula" and x ==""  else x
x = "Bolton" if desc == "esfolado" and x ==""  else x
x = "Tully" if desc == "turta" and x ==""  else x

print("Entrada: ",desc)
if x != "":
	print("Casa: ",x)
else:
	print("Brasao invalido")
	