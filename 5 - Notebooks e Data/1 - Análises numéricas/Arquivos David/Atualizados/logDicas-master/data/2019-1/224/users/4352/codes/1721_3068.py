arma = input("escolha sua arma: ").upper()
D = int(input("digite sua destreza: "))
d1 = int(input("digite o valor sorteado no dado 1: "))
d2 = int(input("digite o valor sorteado no dado 2: "))
soma = d1 + d2
cimi = 2 * soma + 2 * D
kata = 2 * soma + D
sabr = soma + 2 * D
if arma == "CIMITARRA" and D>0 and(10>=d1>1) and (10>=d2>=1):
	print(cimi)
elif arma == "KATANA" and D>0 and(10>=d1>=1) and (10>=d2>=1):
	print(kata)
elif arma == "SABRE" and D>0 and(10>=d1>=1) and (10>=d2>=1):
	print(sabr)
else:
	print("Entrada invalida")