#quantidade inicial de guerreiros na infantaria
qii=int(input("infantaria: "))
#quantidade inicial de de guerreiros da cavalaria
qic=int(input("cavalaria: "))
#percentual de crescimento de tropas infantaria
pci=float(input("percentual de crescimento mensal: "))/100
#percentual de crescimento de tropas da cavalaria
pcc=float(input("percentual de crescimento mensal: "))/100
#variavel contadora
m = 0
x = qic + qii
t = 50000
while ( x < t ):
	qii = qii + ( qii * pci)
	qic = qic + ( qic * pcc)
	x = qii + qic
	m = m + 1
	
print(m)
