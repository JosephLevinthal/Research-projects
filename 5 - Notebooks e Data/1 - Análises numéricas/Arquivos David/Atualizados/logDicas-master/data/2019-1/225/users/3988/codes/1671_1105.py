# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
n = input("entrada:")
if((n!="lobo")and(n!="leao")and(n!="veado")and(n!="dragao")and(n!="rosa")and(n!="sol")and(n!="lula")and(n!="esfolado")and(n!="turta")):
	s = "Brasao "
	d = "invalido"
elif(n=="lobo"):
	s = "Casa: " 
	d = "Stark"
elif(n=="leao"):
	s = "Casa: "
	d = "Lannister"
elif(n=="veado"):
	s = "Casa: "
	d = "Baratheon"
elif(n=="dragao"):
	s = "Casa: "
	d = "Targaryen"
elif(n=="rosa"):
	s = "Casa: "
	d = "Tyrell"
elif(n=="sol"):
	s = "Casa: "
	d = "Martell"
elif(n=="lula"):
	s = "Casa: "
	d = "Greyjoy"
elif(n=="esfolado"):
	s = "Casa: "
	d = "Bolton"
else:
	s = "Casa: "
	d = "Tully"
print("Entrada: ", n)
print(s,d)
	