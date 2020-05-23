va=int(input("cedula"))

if(va==2): 
	p="Tartaruga"
elif(va==5):
	p="Garca"
elif(va==10):
	p="Arara"
elif(va==20):
	p="Mico-leao-dourado"
elif(va==50):
	p="Onca-pintada"
elif(va==100):
	p="Garoupa"
else:
	p="Invalido"


print("Entrada:", va)	
print("Animal:", p)