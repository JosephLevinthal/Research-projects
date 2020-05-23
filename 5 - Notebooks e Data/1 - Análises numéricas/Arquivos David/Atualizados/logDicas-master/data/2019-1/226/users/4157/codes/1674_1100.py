# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
ced = int(input("valor de uma cedula:"))
tart = 2
garca = 5
arara = 10
mld = 20
op = 50
garoupa = 100
if(ced == tart):
	print("Entrada: 2")
	print("Animal: Tartaruga")
elif(ced == garca):
	print("Entrada: 5")
	print("Animal: Garca")
elif(ced == arara):
	print("Entrada: 10")
	print("Animal: Arara")
elif(ced == mld):
	print("Entrada: 20")
	print("Animal: Mico-leao-dourado")
elif(ced == op):
	print("Entrada: 50")
	print("Animal: Onca-pintada")
elif(ced == garoupa):
	print("Entrada: 100")
	print("Animal: Garoupa")
else:
	print("Entrada:", ced)
	print("Animal: Invalido")
	
