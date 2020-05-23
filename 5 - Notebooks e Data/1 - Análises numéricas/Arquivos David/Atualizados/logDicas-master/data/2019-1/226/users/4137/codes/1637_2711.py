vl = float(input("Quanto voce tem:"))
qtru = int(input("Quantos tickets do RU deseja:"))
vlru = float(input("Valor dos tickets:"))
qtps = int(input("Quantidade de passes de onibus:"))
vlps = float(input("Valor dos passes:"))

x = vl - ( qtru * vlru ) - ( qtps * vlps )

if(x >= 0):
	msg = "SUFICIENTE"
else:
	msg = "INSUFICIENTE"
print(msg)	