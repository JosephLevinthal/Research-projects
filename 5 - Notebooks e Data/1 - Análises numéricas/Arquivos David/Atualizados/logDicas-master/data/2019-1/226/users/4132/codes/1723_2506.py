qi = int(input("Digite a quantidade inicial: "))
pc = float(input("Digite o percenrual anual: "))/100
qr = int(input("Digite a quantidade retirada anualmente: "))
soma = qi
cont =0
while(soma>0 and soma<12000):
	soma = soma + (soma*pc) -qr
	cont= cont+1

if(soma<0):
	print("EXTINCAO")
	print(cont)
else:
	print("LIMITE")
	print(cont)
   