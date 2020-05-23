v=int(input("entre com o valor da cedula: "))
a="Animal:"
print("Entrada:",v)
if((v!=2)and(v!=5)and(v!=10)and(v!=20)and(v!=50)and(v!=100)):
	print(a,"Invalido")
elif(v==2):
	print(a,"Tartaruga")
elif(v==5):
	print(a,"Garca")
	
elif(v==10):
	print(a,"Arara")
	
elif(v==20):
	print(a,"Mico-leao-dourado")
	
elif(v==50):
	print(a,"Onca-pintada")
	
elif(v==100):
	print(a,"Garoupa")