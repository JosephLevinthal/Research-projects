x = int(input( "valor da cedula: "))
print("Entrada: ",x)

if(x != 2 and x != 5 and x != 10 and x != 20 and x != 50 and x != 100 ):
	y = "Invalido"
elif(x==2):
   y = "tartaruga"
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
	
print("Animal: ", y)

