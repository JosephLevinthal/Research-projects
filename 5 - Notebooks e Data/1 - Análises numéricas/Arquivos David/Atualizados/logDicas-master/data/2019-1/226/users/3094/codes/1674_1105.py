# Teste seu código aos poucos. Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo. Teste as diversas possibilidades de saída
b = input("brasao: ")
print("Entrada: ", b)
if(b == "lobo"):
	y = "Casa: Stark"
elif(b =='leao'):
	y = "Casa: Lannister"
elif(b == 'veado'):
	y = "Casa: Baratheon"
elif(b == 'dragao'):
	y="Casa: Targaryen"
elif(b == 'rosa'):
	y="Casa: Tyrell"
elif(b  == 'sol' ):
	y="Casa: Martell"
elif(b == 'lula'):
	y= "Casa: Greyjoy"
elif(b == 'esfolado'):
	y="Casa: Bolton"
elif(b == 'turta'):
	y="Casa: Tully"
else:
	y = "Brasao invalido"

print(y)
	
	
	
	
	