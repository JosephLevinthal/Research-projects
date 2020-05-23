escala = input("Digite escala celcius ou fahrenheit: ")
temperatura = float(input("Digite a temperatura: "))

if(escala.lower() == "f"):
	x = 5/9 * ( temperatura - 32 )
	
if(escala.lower() == "c"):
	x = ( 9/5 * temperatura ) + 32
	
print(round(x,2))