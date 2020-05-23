# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.

a = int(input("valor da cedula: "))

print("Entrada:" , a ) 

if (a > 100) or (a < 0):
	print("Animal : invalido")
elif (a == 2):
	print("Animal: Tartaruga")
elif (a==5):
	print("Animal: Garca")
elif(a==10):
	print("Animal: Arara")
elif (a==20):
	print("Animal : Mico-leao-dourado")
elif(a==50):
	print("Animal: Onca-pintada")
elif (a==100):
	print("Animal: Garoupa")
else:
	print("Animal: Invalido")
	