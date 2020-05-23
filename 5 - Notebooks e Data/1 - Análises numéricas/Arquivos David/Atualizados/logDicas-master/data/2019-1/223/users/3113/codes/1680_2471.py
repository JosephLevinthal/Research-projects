a=int(input("idade:"))
b=float(input("IMC:"))
z="Baixo"
x="Medio"
c="Alto"
print("Entradas:", a, "anos e IMC", b)
if(a<=0 or a>130 or b<=0):
	print("Dados invalidos")
elif(a<45 and b<22.0):
	print("Risco:",z)
elif(a<45 and b>=22.0):
	print("Risco:",x)
elif(a>=45 and b<22.0):
	print("Risco:",x)
elif(a>=45 and b>=22.0):
	print("Risco:",c)