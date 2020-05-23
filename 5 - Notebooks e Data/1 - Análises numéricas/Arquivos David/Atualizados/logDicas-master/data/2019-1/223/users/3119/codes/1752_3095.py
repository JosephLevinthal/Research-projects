resultado = input("Resultado da partida: ")

v = 0
e = 0
d = 0

while(resultado.upper() != "X"):
	if(resultado.upper() == "V"):
		v = v + 3 
	elif(resultado.upper() == "E"):
		e = e + 2
	elif(resultado.upper() == "D"):
		d = d + 1
		
	resultado = input("Resultado da partida: ")
	
print(v)
print(e)
print(d)