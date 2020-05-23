qo= int(input("Digite: "))
pc = float(input("Digite: "))/100

cont=0
soma = qo
while(soma>0 and soma<8000):
	pr = int(input("Digite: "))
	soma = soma + (soma*pc) - pr
	cont= cont +1
	if(soma<0):
	print("ZERO")
	print(cont)
else:
	print("MAXIMO")
	print(cont)