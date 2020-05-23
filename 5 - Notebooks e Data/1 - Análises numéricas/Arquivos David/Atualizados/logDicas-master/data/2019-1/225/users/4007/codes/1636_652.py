a = int(input("digite um numero: (0 a 9) "))
b = int(input("digite um numero: (10 a 90)"))
c = int(input("digite um numero: (100 a 900)"))
d = a + b + c
if(100 >= d and d <= 999):
	e = d / a - b + c
	print("SIM")
	