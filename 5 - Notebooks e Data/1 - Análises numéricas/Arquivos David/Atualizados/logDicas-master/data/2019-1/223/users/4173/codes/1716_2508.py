a = int(input())
n = 2
k = 1
sinal = 1
acr = 0
while k < a:
	acr = acr +  sinal*(4/((n)*(n+1)*(n+2)))	
	sinal = sinal*(-1)
	n += 2
	k += 1
acr = 3+acr
print(round(acr,8))