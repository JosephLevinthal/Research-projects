# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.

v = int(input("Qual o valor da cedula:"))
print("Entrada:", v)
if(v == 2):
	print("Animal: Tartaruga")
elif(v == 5):
	print("Animal: Garca")
elif(v == 10):
	print("Animal: Arara")
elif(v == 20):
	print("Animal: Mico-leao-dourado")
elif(v == 50):
	print("Animal: Onca-pintada")
elif(v == 100):
	print("Animal: Garoupa")
elif(v != 2 and v != 5 and v!= 10 and v!= 20 and v!=50 and v!=100 ):
	print("Animal: Invalido")
	