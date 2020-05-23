valortotal=float(input("digite o valor:"))
R=(valortotal<=500*0,44) or (valortotal>=500*0,65)
C=(valortotal<=1000*0,55) or (valortotal>=1000*0,60)
I=(valortotal<=5000*0,55) or (valortotal>=5000*0,60)
if(valortotal<=500kwh*0,44):
	mensagem="tipo R".upper()
elif(valortotal>=500kwh*0,65):
	mensagem="tipo R".upper()	
elif(valortotal<=1000kwh*0,55):
	mensagem="tipo C".upper()
elif(valortotal>=1000kwh*0,60):
	mensagem="tipo C".upper()
elif(valortotal<=5000kwh*0,55):
	mensagem="tipo I".upper()
elif(valortotal>=5000kwh*0,60):
	mensagem="tipo I".upper()
else:
	mensagem="Dados invalidos"
print("Entrada:", valortotal ,",", mensagem)
print("Valor total:", c)
