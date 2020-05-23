tam = float(input("Quant. de peixes: "))
P_cres = float(input("Percentual de cres: "))
q = int(input("Quant. para vendas: "))
 
anos = 0

while( tam > 0 and tam < 12000):
	y = tam * P_cres / 100
	tam = tam + y - q
	anos = anos + 1
if(tam >= 12000):
	print("LIMITE")
elif(tam <= 0):
	print("EXTINCAO")
print(anos)


	