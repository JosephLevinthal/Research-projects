# Ao testar sua solução, não se limite ao caso de exemplo.
x = float(input())
y = float(input())

if(y >= 0.0 and ((x >= 0.0) or (x < 0))):
	print("Superiores")
else:
	print("Inferiores")