#fazer terminar a soma digitando 0
#media dos numeros pares e a media dos numeros impares
x = int(input("digite o numero inteiro: "))
spar = 0
simp = 0
i = 0
while(x!=0):
	if(x%2==0):
		spar = spar + x
		i = i + 1
	elif(x%2!=0):
		simp = simp + x
		i = i + 1 
	x = int(input("digite o numero inteiro: "))
spar = spar/i
simp = simp/i
print(round(spar,2))
print(round(simp,2))