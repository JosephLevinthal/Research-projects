
# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
valor= int(input("valor da cedula: "))

print("Entrada:", valor)

if ((valor!=2) and (valor!=5) and (valor!=10) and (valor!=20) and (valor!=50) and (valor!=100)):
	print("Animal: Invalido")
elif(valor==2):
	print("Animal: Tartaruga")
elif(valor==5):
	print("Animal: Garca")
elif(valor==10):
	print("Animal: Arara")
elif(valor==20):
	print("Animal: Mico-leaodourado")
elif(valor==50):
	print("Animal: Onca-pintada")
elif(valor==100):
	print("Animal: Garoupa")