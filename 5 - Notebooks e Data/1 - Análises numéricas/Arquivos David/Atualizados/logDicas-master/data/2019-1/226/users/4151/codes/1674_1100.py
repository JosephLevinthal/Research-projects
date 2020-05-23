x=int(input("valor da cedula: "))
y="Animal:"
print("Entrada:",x)
if(x!=2 and x!=5 and x!=10 and x!=20 and x!=50 and x!=100):
	print(y,"Invalido")
elif(x==2):
	print(y,"Tartaruga")
elif(x==5):
	print(y,"Garca")
elif(x==10):
	print(y,"Arara")
elif(x==20):
	print(y,"Mico-leao dourado")
elif(x==50):
	print(y,"Onca-pintada")
elif(x==100):
	print(y,"Garoupa")
	
