x = float(input("quantos bonoros tu tens? "))
v = int(input("quantos ticket? "))
v2 = float(input("quanto vale o R.U? "))
x1 = int(input("quantos passes? "))
x3 = float(input("quantos bonossauro vale o passe? "))
x4 = (v*v2) + (x1*x3) 
if (x>=x4):
	print("suficiente".upper())
else:
	print("insuficiente".upper())