# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.

a=int(input("Entrada: "))
print("Entrada:",a)
if((a!=2)and(a!=5)and(a!=10)and(a!=20)and(a!=50)and(a!=100)):
	print("Animal: Invalido")
elif(a==2):
	print("Animal: Tartarura")
elif(a==5):
	print("Animal: Garca")
elif(a==10):
	print("Animal: Arara")
elif(a==20):
	print("Animal: Mico-leao-dourado")
elif(a==50):
	print("Animal: Onca-pintada")
else:
	print("Animal: Garoupa")