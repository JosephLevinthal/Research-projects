nta = float(input("Qual sua nota:"))
bnf = input("Voce recebe bonificacao:")

if (bnf.upper() == "S"):
	bnf1 = nta*(10/100)
	msg = nta + bnf1
else:
	msg = nta

print(msg)