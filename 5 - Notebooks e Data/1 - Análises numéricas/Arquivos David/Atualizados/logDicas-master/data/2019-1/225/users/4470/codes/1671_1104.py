a = float(input(""))
b = float(input(""))
c = float(input(""))
d = float(input(""))
print( " Intervalo 1:", a , "," , b)
print( " Intervalo 2:", c , "," , d)
if ( b > a ) and (d > c) :
	if (( (c < a) and (d < a)) or (( d > b ) and (c > b) )) :
		print("Nao ha intersecao")
	else :
		print("Ha intersecao")
else :
	print("Entradas invalidas")
