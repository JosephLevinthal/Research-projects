qit = int(input("inicial de tambaquis: "))
pc = int(input("crescimento anual: "))/100
qr = int(input("tambaquis vendidos anualmente: "))

ano = 0
while (qit > 0 and  qit < 12000):
	qit = qit + (qit * pc) - qr
	ano = ano + 1
	
if (qit <= 0):
	print("EXTINCAO")
	
elif(qit >= 12000):
	print("LIMITE")

print(ano)


	