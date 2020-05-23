c = int(input("Valor da cedula: "))
if(c == 2):
	a = "Tartaruga"
elif(c == 5):
	a = "Garca"
elif(c == 10):
	a = "Arara"
elif(c == 20):
	a = "Mico-leao-dourado"
elif(c == 50):
	a = "Onca-pintada"
elif(c == 100):
	a = "Garoupa"
else: 
	a = "Invalido"
	
print("Entrada:", c)
print("Animal:", a)