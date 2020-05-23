# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.

#Uma entrada com valor real inteiro(representando a nota)
valor_nota=int(input("valor da nota :"))
#Sera um if, elife para cada nota e por ultimo o else sera se " Animal: Invalido"
if (valor_nota == 2) :
	print("Entrada:" , valor_nota)
	print("Animal: Tartaruga")
elif (valor_nota == 5) :
	print("Entrada:" , valor_nota)
	print("Animal: Garca")
elif (valor_nota == 10) :
	print("Entrada:" , valor_nota)
	print("Animal: Arara")
elif (valor_nota == 20) :
	print("Entrada:" , valor_nota)
	print("Animal: Mico-leao-dourado")
elif (valor_nota == 50) :
	print("Entrada: " , valor_nota)
	print("Animal: Onca-pintada")
elif (valor_nota == 100) :
	print("Entrada:" , valor_nota)
	print("Animal: Garoupa")
	
else :
	print("Entrada:" , valor_nota)
	print("Animal: Invalido")