qv = int(input("Digite a quantodade de virus: "))
ql = int(input("Digite a quantodade de leucocitos: "))
pv = float(input("Digite o percentual de virus: "))/100
pl = float(input("Digite o percentual de leucocitos: "))/100
cont = 0
soma = qv
soma2 = ql
while(soma2 < 2*soma):
	soma = soma + (soma * pv)
	soma2 = soma2 + (soma2*pl)
	cont = cont+1
print(cont)

