# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
a=int(input("valor de a:" ))
print("Entrada:",a)		
if(a==2)or(a==5)or(a==10)or(a==20)or(a==50)or(a==100):
	if (a==2):
		print("Animal: Tartaruga")
	elif (a==5):
		print("Animal: Garca")
	elif(a==10):
		print("Animal: Arara")
	elif(a==20):
		print("Animal: Mico-leao-dourado")
	elif(a==50):
		print("Animal: Onca-pintada")
	elif(a==100):
		print("Animal: Garoupa")
else:
	print("Animal: Invalido")
		