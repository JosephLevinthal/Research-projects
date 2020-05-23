# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.

cedula = int(input("Valor da cedula: "))

print("Entrada:", cedula)

if(cedula == 2):
	print("Animal: Tartaruga")
elif(cedula == 5):
	print("Animal: Garca")
elif(cedula == 10):
	print("Animal: Arara")
elif(cedula == 20):
	print("Animal: Mico-leao-dourado")
elif(cedula == 50):
	print("Animal: Onca-pintada")
elif(cedula == 100):
	print("Animal: Garoupa")
else:
	print("Animal: Invalido")