k = int(input("numero de termos: "))
a1 = 2
a2 = 3
a3 = 4
i = 0
termo = 0
if(k == 1):
	print("3")
else:
	while(i+1<k):
		sinal = (-1)**i
		termo = termo + sinal*(4/(a1*a2*a3))
		a1 = a1 + 2
		a2 = a2 + 2
		a3 = a3 + 2
		i = i + 1

print(round(3 + termo,8))