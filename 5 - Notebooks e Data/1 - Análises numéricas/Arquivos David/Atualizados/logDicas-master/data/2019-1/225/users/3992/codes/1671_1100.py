# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.

nota = int(input("Valor da cedula:"))
print("Entrada: ", nota)
if(nota==2):
	print("Animal: tartaruga")
elif(nota==5):
	print("Animal: garca")
elif(nota==10):
	print("Animal: arara")
elif(nota==20):
	print("Animal: Mico-leao-dourado")
elif(nota==50):
	print("Animal: Onca-pintada")
elif(nota==100):
	print("Animal: Garoupa")
else:
	print("Animal: Invalido")