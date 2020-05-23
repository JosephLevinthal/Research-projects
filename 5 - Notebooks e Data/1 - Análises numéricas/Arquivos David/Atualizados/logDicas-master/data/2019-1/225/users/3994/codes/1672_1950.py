t=float(input("Digite a temperatura do ar: "))
v=float(input("Digite a velocidade do vento: "))

j= ((13.12 + 0.6215 * t) - (11.37 *(v)**0.16) + (0.3965 * t * (v)**0.16))
if(t<=-50 and t>10):
	mensagem="Temperatura invalida"
	print(mensagem)
elif(v<=4.8):
	mensagem="Velocidade invalida"
	print(mensagem)
	
