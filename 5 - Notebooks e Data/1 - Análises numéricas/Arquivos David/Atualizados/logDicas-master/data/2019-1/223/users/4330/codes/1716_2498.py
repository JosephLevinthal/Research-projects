A = int(input("numero de hab de A: "))
B = int(input("numero de hab de B: "))
PA = float(input("crescimento populacional A: "))
PB = float(input("crescimento populacional B: "))
#variavel contadora
anos = 0

while ( A < B ):
	A = A + ( A * (PA/100) )
	B = B + ( B * (PB/100) )
	anos += 1
	
print(anos)