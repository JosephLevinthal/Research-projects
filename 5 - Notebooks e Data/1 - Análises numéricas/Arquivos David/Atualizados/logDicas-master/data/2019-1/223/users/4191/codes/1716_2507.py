qi=int(input("Quantidade inical de peixe: "))
pc=int(input("Percentual de crescimento: "))


cont=0


while(0<qi<8000):
	pr=int(input("Peixes retirados por mes: "))
	cresc= qi * (pc/100)
	qi= qi+cresc
	qi= qi - pr
	cont=cont+1

if(qi<=0):
	print('ZERO')
else:
	print('MAXIMO')

	
print(cont)	
	