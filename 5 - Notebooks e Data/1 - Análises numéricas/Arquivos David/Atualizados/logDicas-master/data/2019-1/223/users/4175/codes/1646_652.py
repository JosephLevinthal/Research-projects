n = int(input())

b = (n%100)

d = n%b

if d == 0:
	print("SIM")
else:
	print("NAO")