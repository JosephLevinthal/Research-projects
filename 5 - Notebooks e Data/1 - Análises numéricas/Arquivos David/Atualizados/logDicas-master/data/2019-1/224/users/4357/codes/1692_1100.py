cedula=int(input("digite o numero:"))
animal= "burro"
if(cedula==2):
	animal="Tartaruga"
elif(cedula==5):
	animal="Garca"
elif(cedula==10):
	animal="Arara"
elif(cedula==20):
	animal="Mico-leao-dourado"
elif(cedula==50):
	animal="Onca-pintada"
elif(cedula==100):
	animal="Garoupa"
else:
	animal="Invalido"
print("Entrada:", cedula)
print("Animal:", animal)

