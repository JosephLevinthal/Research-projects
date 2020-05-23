qi = int(input("Qi: "))
perc = int(input("perc: "))
quant = int(input("Quantidade: "))

ano = 0
cap = 12000

while(qi < cap) and (qi > 0):
	qi = qi + (qi * perc/100) - quant
	ano = ano + 1
if(qi < 0):
	print("EXTINCAO")
if(qi > 0):
	print("LIMITE")

print(ano)