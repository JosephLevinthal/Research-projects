# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
c = int(input("Digite o valor de cedula: "))

print("Entrada:", c )
if (c!=2 and c!=5 and c!=10 and c!=20 and c!=50 and c!=100):
	print("Animal: Invalido")	
elif (c==2):
	print("Animal: Tartaruga")
elif (c==5):
	print("Animal: Garca")
elif (c==10):
	print("Animal: Arara")
elif (c==20):
	print("Animal: Mico-leao-dourado")
elif (c==50):
	print("Animal: Onca-pintada")
elif (c==100):
	print("Animal: Garoupa")
	