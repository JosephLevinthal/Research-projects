

x = float(input())

if( x <= 0):
	print(0)
if( 0 < x <= 1 ):
	print(1)
if(1 < x <= 2 ):
	print(round(x**(0.5),4))
if(x > 2):
	print(round( x**(3/9), 4 ))