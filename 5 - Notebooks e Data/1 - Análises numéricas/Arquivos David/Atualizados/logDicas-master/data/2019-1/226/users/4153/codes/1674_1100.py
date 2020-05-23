# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
vdc = int(input("Insira o valor da cedula: "))
print("Entrada:", vdc)

if((vdc != 2) and (vdc != 5) and (vdc != 10) and (vdc != 20) and (vdc != 50) and (vdc != 100)):
	print("Animal: Invalido")
elif(vdc == 2):
	print("Animal: Tartaruga")
elif(vdc == 5):
	print("Animal: Garca")
elif(vdc == 10):
	print("Animal: Arara")
elif(vdc == 20):
	print("Animal: Mico-leao-dourado")
elif(vdc == 50):
	print("Animal: Onca-pintada")
elif(vdc == 100):
	print("Animal: Garoupa")
