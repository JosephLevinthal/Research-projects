# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
a=input("Entrada: ")
print("Entrada:", a)
if((a!="lobo")and(a!="leao")and(a!="veado")and(a!="dragao")and(a!="rosa")and(a!="sol")and(a!="lula")and(a!="esfolado")and(a!="turta")):
	print("Brasao invalido")
elif(a=="lobo"):
	print("Casa: Stark")
elif(a=="leao"):
	print("Casa: Lannister")
elif(a=="veado"):
	print("Casa: Baratheon")
elif(a=="dragao"):
	print("Casa: Targaryen")
elif(a=="rosa"):
	print("Casa: Tyrell")
elif(a=="sol"):
	print("Casa: Martell")
elif(a=="lula"):
	print("Casa: Greyjoy")
elif(a=="esfolado"):
	print("Casa: Bolton")
elif(a=="turta"):
	print("Casa: Tully")