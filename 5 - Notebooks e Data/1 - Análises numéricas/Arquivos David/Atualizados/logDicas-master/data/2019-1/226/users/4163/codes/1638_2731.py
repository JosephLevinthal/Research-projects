a = float(input("abcissas: "))
b = float(input("ordenadas: "))
r = float(input("raio: "))


x = a**2-(r**2/2)
y = b**2-(r**2/2)

if (b > 0 ):
	print("Superiores")
elif(b<0 ) :
	print("Inferiores")
