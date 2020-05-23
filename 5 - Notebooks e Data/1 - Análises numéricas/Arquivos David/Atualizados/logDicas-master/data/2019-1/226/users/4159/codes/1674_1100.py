x = (int(input("nota: ")))
print("Entrada:",x)
if((x==2)or(x==5)or(x==10)or(x==20)or(x==50)or(x==100)):
	if(x==2):
		y = "Tartaruga"
	elif(x==5):
		y = "Garca"
	elif(x==10):
		y = "Arara"
	elif(x==20):
		y = "Mico-leao-dourado"
	elif(x==50):
		y = "Onca-pintada"
	elif(x==100):
		y = "Garoupa"
else:
	y = "Invalido"
print("Animal: "+y)
