# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.

x= int(input ("Digite o valor de uma cedula R$ 2, 5, 10, 20, 50 ou 100:  "))
print ("Entrada:",x)

if x != 2 and x !=5 and x !=10 and x !=20 and x !=50 and x !=100:
	print ("Animal: Invalido")
elif (x==2):
	print ("Animal: Tartaruga")
elif (x==5):
	print ("Animal: Garca")
elif (x==10):
	print ("Animal: Arara")
elif (x==20):
	print ("Animal: Mico-leao-dourado")
elif (x==50):
	print ("Animal: Onca-pintada")
elif (x==100):
	print ("Animal: Garoupa")