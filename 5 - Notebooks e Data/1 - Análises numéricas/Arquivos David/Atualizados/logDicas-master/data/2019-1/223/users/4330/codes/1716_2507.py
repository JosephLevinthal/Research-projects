qi=int(input("quantidade de inicial: "))
pc=int(input("percentual de crescimento mensal: "))

meses = 0
while( 0 < qi < 8000):
	qprv=int(input("Quantidade de peixes retirados para venda mensal:"))
	qi = qi + ( qi * ( pc /100 ))
	qi = qi - qprv
	meses = meses + 1
	if ( qi <= 0 ):
		print("ZERO")
	elif ( qi >= 8000 ):
		print("MAXIMO")
print(meses)