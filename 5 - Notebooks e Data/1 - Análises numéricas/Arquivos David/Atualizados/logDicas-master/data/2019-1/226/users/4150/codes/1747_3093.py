r = input("resultado V/D/E?: ").upper()

x = 0
y = 0

while(r != "X"):
	if ( r == "V"):
		x = x + 1
	
	elif ( r == "E"):
		y = y + 1
		
	r = input("resultado V/D/E?: ").upper()

print(x * 3)
print(y * 1)