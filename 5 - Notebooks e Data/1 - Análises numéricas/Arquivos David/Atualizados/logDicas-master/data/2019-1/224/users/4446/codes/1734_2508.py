n=int(input("numero de termos: "))
i=0
soma=0
y=2
j=3
k=4
if(n==1):
	print("3")
else:
	while(i+1<n):
		sinal= (-1)**i
		soma= soma + sinal * (4/(y * j * k))
		y= y + 2
		j= j + 2
		k= k + 2
		i= i + 1
print(round(soma + 3, 8))