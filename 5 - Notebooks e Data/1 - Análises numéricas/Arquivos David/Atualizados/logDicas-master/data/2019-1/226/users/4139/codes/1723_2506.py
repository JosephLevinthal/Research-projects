qi = int(input("quantidade inicial de tambaquis no tanque: "))
pc = int(input("percentua de crescimento anual: "))
qv = int(input("quantidade de tambaquis retirados para venda: "))

p = pc / 100

ano = 0

while(qi < 12000 and qi > 0):
	qi += (qi*p)-qv
	ano = ano + 1

if(qi >= 12000):
	print("LIMITE")
else:
	print("EXTINCAO")
print(ano)