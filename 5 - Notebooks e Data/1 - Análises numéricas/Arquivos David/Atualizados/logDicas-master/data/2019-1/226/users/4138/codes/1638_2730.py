# Ao testar sua solução, não se limite ao caso de exemplo.
x = float(input("insira a coordernada x:"))
y = float(input("insira a coordernada y:"))

if (x > 0 and y > 0):
	print("Superiores")
if ( x < 0 and y > 0):
	print("Superiores")
if (x > 0 and y < 0):
	print("Inferiores")
if (x < 0 and y < 0):
	print("Inferiores")