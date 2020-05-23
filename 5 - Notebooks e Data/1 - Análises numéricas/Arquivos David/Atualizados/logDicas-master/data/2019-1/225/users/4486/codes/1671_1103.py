x = float(input())
a = float(input())
b = float(input())

if (a <= x) and (x <= b):
	print (x, "pertence ao intervalo", a, ",", b)	
elif(b <= a):
	print ("entradas", a, " e ", b, "invalidas")
else:
	print (x, "nao pertence ao intervalo", a, ",", b)