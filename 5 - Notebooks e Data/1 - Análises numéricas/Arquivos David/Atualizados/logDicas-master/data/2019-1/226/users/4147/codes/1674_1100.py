# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.

valor = int(input("Valor de uma cedula: "))
print("Entrada:" , valor,)
if( valor == 2 ):
	print("Animal: Tartaruga")
elif( valor == 5 ):
	print("Animal: Garça")
elif( valor == 10):
	print("Animal: Arara")
elif( valor == 20):
	print("Animal: Mico-leao-dourado")
elif( valor == 50):
	print(" Animal: Onca-pintada")
elif( valor == 100):
	print(" Animal: Garoupa")
else:
	print("Animal: Invalido")