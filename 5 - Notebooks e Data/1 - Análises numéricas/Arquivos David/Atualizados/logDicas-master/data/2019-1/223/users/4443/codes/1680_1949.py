#Leitura dos numeros apostados pelo jogador com dois digitos:
j = int(input("digite um numero com dois digitos: "))
l = int(input("digite um numero com dois digitos: "))
dj = j//10 
uj = j%10
dl = l//10
ul = l%10

if(j == l):
	print("Ganhou R$ 100.000,00")
elif(uj == dl) and (dj == ul):
	print("Ganhou R$ 50.000,00")
elif(dj == dl) or (dj == ul) or (uj == dl) or (uj == ul):
	print("Ganhou R$ 1.000,00")
else:
	print("Perdeu")