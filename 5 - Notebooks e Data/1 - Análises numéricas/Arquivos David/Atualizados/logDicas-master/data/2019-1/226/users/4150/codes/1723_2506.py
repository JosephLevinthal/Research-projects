qt = int(input("no inicial de tambaquis: "))
pc = int(input("percentual: "))
qr = int(input("quantidade retirada: "))

ano = 0
cap = 12000

while (qt < cap) and (qt > 0):
	qt = qt + (qt*(pc/100)) - qr	
	ano = ano + 1
	
if (qt < 0):
	print("EXTINCAO")
if(qt > cap):
	print("LIMITE")

print(ano)