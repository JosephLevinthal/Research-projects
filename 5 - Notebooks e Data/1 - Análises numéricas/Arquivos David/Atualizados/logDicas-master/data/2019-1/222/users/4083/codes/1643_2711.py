valod = float(input("valor disponivel: "))
quatr = int(input("tickets do ru: "))
valot = float(input("valor do ru: "))
quanps = int(input("quantidades de passes de onibus: "))
valordopasse = float(input("valor do onibus: "))

gastos = (quatr*valot + quanps*valordopasse)

if  (valod >= gastos):
     print("SUFICIENTE")
		
else:
	 print("INSUFICIENTE")