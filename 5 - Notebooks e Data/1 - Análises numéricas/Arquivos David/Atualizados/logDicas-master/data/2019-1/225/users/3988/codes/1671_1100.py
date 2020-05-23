# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Ao testar sua solução, não se limite ao caso de exemplo.
R = int(input("R$:"))
if(R!=2)and(R!=5)and(R!=10)and(R!=20)and(R!=50)and(R!=100):
	msg = "Animal: Invalido"
elif(R ==2):
	msg = "Animal: Tartaruga"
elif(R == 5):
	msg = "Animal: garca"
elif(R ==10):
	msg = "Animal: Arara"
elif(R == 20):
	msg = "Animal: Mico-leao-dourado"
elif(R == 50):
	msg = "Animal: Onca-pintada"
else:
	msg = "Animal: Garoupa"
print("Entrada: ",R)	
print(msg)