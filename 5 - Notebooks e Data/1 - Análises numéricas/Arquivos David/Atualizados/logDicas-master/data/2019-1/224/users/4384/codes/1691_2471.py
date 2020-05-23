x=int(input("digite a idade:"))
y=float(input("digite imc:"))
if((x<=0)or(x>130)or(y<=0)):
	print("Entradas:",x,"anos e IMC",y)
	print("Dados invalidos")
elif((x<45)and(y<22)):
	z="Baixo"
elif((x>=45)and(y<22)):
	z="Medio"
elif((x<45)and(y>=22)):
	z="Medio"
elif((x>=45)and(y>=22)):
	z="Alto"
print("Entradas:",x,"anos e IMC",y)
print("Risco:",z)
