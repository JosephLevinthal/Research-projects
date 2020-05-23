var= float(input("valor da compra"))
d= (var*5)/100

if ( var >= 200):
	print(round( var - d,2))
	
else:
	print(round(var,2))