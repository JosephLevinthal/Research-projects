#oscilação de menos e mais (-1)**(i)
#aumento de numero impar 
n=int(input())
resultado=0
i=0
while(i<n):
	conta= ((-1)**i)/((1+2*i)*3**i)
	resultado=resultado+conta
	i=i+1
final=resultado*12**0.5
print(round(final,8))
