from numpy import*
x = input("digite: ").replace(" ","").upper()
i = -1
a = 0
new = ""
while (a < len(x)):
	if( x[a] == x[i] ):
		new = new + x[i]
		i = i - 1
		a = a + 1
	else:
		msg = 0
		a = a + 1


if x == new:
	print(new) 
	msg = 1
else:
	print(x)
		
print(msg)

	
	
