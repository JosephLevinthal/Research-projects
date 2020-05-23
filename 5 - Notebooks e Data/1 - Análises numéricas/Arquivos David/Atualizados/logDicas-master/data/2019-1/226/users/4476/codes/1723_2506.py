qit = int(input("digite o valor: "))
cat = int(input("digite o valor: "))
qtv = int(input("digite o valor: "))

percat = cat/100
ano = 0

while ((qit > 0) and (qit < 12000)):
	qit = (qit + (qit*percat)) - qtv
	ano = ano + 1
if (qit<0):
	print("EXTINCAO")
if (qit>12000):
	print("LIMITE")

print(ano)
