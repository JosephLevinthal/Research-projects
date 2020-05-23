qif = int(input("quantidade de seguidores de Forseti : "))
qil = int(input("quantidade de seguidores de Loki : "))
paf = float(input("digite o percentual : "))
pal = float(input("digite o percentual : "))
paf , pal = paf/100, pal/100
t = 0
while(qil<qif):
	qif = qif + qif * paf
	qil = qil + qil * pal
	t = t + 1
print(t)