x = float(input("Qual o valor de x?"))

if ( x <= 1):
	fx = 1
	print ( round ( fx, 2) )
elif ( ( 1 < x ) and (x <= 2) ):
	fx = 2
	print ( round( fx, 2) )
elif ( ( 2 < x ) and ( x <= 3 ) ):
	fx = x**2
	print ( round( fx, 2) )
else:
	fx = x**3
	print ( round( fx, 2) )
