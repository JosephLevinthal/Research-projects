n = int(input("Digite um numero inteiro: "))
h = 0
for i in range(n):
	h = h + ((-1)**i)*(1/(1+i))
h = round(h, 6)
print("H = ",h)	
		  