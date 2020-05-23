QFor = int(input("quantidade inicial de seguidores do deus Forseti:"))
QLoki = int(input("quantidade inicial de seguidores do deus Loki:"))
PACFor = float(input("percentual anual de crescimento dos seguidores do deus Forseti:"))/100
PACLoki = float(input("percentual anual de crescimento dos seguidores do deus Loki"))/100

anos = 0
while(QLoki < QFor ):
	QFor = QFor + (QFor * PACFor)
	QLoki = QLoki + (QLoki * PACLoki)
	anos = anos + 1
print(anos)