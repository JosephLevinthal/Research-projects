n = int(input("numero: "))
a = n // 100
a1 = n % 100
b = a1 // 10
b1 = a1 % 10
c = b1 // 1
c1 = b1 % 1
x = n / n - a1

n = 100 <= n <= 999
if (x == 0):
	print("SIM")
else:
	print("NAO")