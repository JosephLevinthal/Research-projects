valor= float(input())
tockets = int(input())
valort = float(input())
busao= int(input())
passe = float(input())
r = (tockets*valort) + (busao*passe)

if (valor > r):
	mensagem = "SUFICIENTE"
else:
	mensagem = "INSUFICIENTE"
print(mensagem)