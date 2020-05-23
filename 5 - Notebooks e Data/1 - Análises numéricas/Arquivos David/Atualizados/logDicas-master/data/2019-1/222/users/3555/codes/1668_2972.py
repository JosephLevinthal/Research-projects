p = int(input())
v = int(input())
t = int(input())

s = p + v*t
if( s >= 1000 - p ):
	print(s)
	print("Sim")
	
if( s < 1000 - p):
	print(s)
	print("Nao")