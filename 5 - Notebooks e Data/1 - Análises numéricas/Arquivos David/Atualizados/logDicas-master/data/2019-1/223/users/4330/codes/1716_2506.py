qi = int(input("quantidade inicial:"))
pc = int(input("percentual de crescimento: "))
qv = int(input("quantidade de vendas: "))

anos = 0 
#qt(quantidade de tambaquis)
qt = qi
while ( 0 < qt < 12000 ):
	qt = qt + ( qt * ( pc / 100 ) )
	qt = qt - qv
	anos += 1
	if ( qt <= 0):
		print("EXTINCAO")
	elif ( qt >= 12000):
		print("LIMITE")
print(anos)