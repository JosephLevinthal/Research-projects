N = int(input("digite um numero: "))

h = 0

for i in range(1,(N+1)):
	h = h + (1/i)
print(round(h,2))
	