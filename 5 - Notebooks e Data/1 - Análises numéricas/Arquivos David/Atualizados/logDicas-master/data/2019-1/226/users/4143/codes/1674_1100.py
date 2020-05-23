a = int(input("digite valor da celula:"))

print("Entrada:", a)
if ((a >100) or (a<0)):
	print("Animal:", "Invalido")
elif (a==2):
	print("Animal:", "Tartaruga")
elif (a==5):
	print("Animal:", "Garça")
elif (a==10):
	print("Animal:", "Arara")
elif (a==20):
	print("Animal:", "Mico-leao-dourado")
elif(a==50):
	print("Animal:", "Onca-pintada")
elif(a==100):
	print("Animal:", "Garoupa")
else:
	print("Animal:", "Invalido")
