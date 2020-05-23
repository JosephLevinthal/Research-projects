# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
vc = int(input("valor de uma cedula:"))
print("Entrada:" , vc)

if((vc != 2) and (vc != 5) and (vc != 10) and (vc != 20) and (vc != 50) and (vc != 100)):
	print("Animal: Invalido")
elif (vc == 2):
	print( "Animal: Tartaruga")
elif (vc == 5):
	print( "Animal: Garca ")
elif (vc == 10):
	print( "Animal: Arara")
elif (vc == 20):
	print( "Animal: Mico-leao-dourado")
elif (vc == 50):
	print( "Animal: Onca-pintada")
elif (vc == 100):
	print( "Animal: Garoupa")