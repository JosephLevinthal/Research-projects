n = int(input("numero inteiro: "))
x = n - (n//100)*100
d = n/x
i = int(n/x)
if (d == i):
	print("SIM")
else:
	print("NAO")
