valord=float(input("valor: "))
qtru=int(input("qt de fichas no RU: "))
valorru=float(input("valor dos tickets RU: "))
qtpass=int(input("qt de passe estudantil: "))
valorpass=float(input("valor do passe estudantil: "))

if (valord >= ((qtru*valorru)+(qtpass*valorpass))):
	print("SUFICIENTE")
else:
	print("INSUFICIENTE")
	