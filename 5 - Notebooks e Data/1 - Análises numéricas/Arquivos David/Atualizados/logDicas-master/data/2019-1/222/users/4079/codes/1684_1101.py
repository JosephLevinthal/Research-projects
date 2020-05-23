# Teste seu código aos poucos.
# Não teste tudo no final, pois fica mais difícil de identificar erros.
# Use as mensagens de erro para corrigir seu código.
x=float(input(":"))
y=input(":")
print("Entradas:", x,"kWh e tipo", y.upper())

if(x>0 and x<=500 and y.upper()=="R"):
	z=x*0.44
	print("Valor total: R$",round(z,2))
elif(x>500 and y.upper()=="R"):
	z=x*0.65
	print("Valor total: R$",round(z,2))
elif(x>0 and x<=1000 and y.upper()=="C"):
	z=x*0.55
	print("Valor total: R$",round(z,2))
elif(x>1000 and y.upper()=="C"):
	z=x*0.60
	print("Valor total: R$",round(z,2))
elif(x>0 and x<=5000 and y.upper()=="I"):
	z=x*0.55
	print("Valor total: R$",round(z,2))
elif(x>5000 and y.upper()=="I"):
	z=x*0.60
	print("Valor total: R$",round(z,2))

else:
	print("Dados invalidos")