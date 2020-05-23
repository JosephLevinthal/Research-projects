suc= int(input("Sucos: "))
sal= int(input("Salgados: "))
valor= float(input("Grana Disponivel: "))

if (valor >= (suc*3)+(sal*3.50)):
	print((suc*3)+(sal*3.50))
	print("Sim")
	
else:
	print((suc*3)+(sal*3.50))
	print("Nao")