qi= int(input("Q. Inicial: "))
pc= int(input("Perc. de Cresc.: "))
qv= int(input("Quant. de Vendas: "))

anos = 0
qt = qi
while ( 0 < qt < 12000 ):
	qt = qt + (qt * ( pc / 100 ))
	qt = qt - qv
	anos = anos + 1
	if (qt <= 0):
		print("EXTINCAO")
	elif (qt >= 12000):
		print("LIMITE")
print(anos)