vi = int(input("Volume inicial: "))
va = int(input("Volume que bombea para dentro: "))
vd = int(input("Volume de agua retirada: "))

min = 0

while(vi > 1000):
	vi = vi + va - vd
	min = min + 1

print(min)