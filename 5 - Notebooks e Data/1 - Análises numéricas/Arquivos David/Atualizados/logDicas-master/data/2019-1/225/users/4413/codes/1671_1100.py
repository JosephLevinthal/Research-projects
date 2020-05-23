a =int(input("valor da cedula: "))
print("Entrada:", a)
if(a==2):
	msg= ("Tartaruga")
elif(a==5):
	msg=("Garca")
elif(a==10):
	msg=("Arara")
elif(a==20):
	msg=("Mico-leao-dourado")
elif(a==50):
	msg=("Onca-pintada")
elif(a==100):
	msg=("Garoupa")
else:
	msg=("Invalido")
print("Animal:", msg)