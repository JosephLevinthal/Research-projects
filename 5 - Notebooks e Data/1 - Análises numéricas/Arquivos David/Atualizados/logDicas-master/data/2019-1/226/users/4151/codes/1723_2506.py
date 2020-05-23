qi=int(input("quantidade de tambaquis: "))
pc=int(input("percentual de tambaquis: "))/100
v=int(input("retirados pra venda: "))
a=0
while(qi>0 and qi<12000):
	qi=(qi+(qi*pc))-v
	a=a+1
	if(qi<0):
		mensagem="EXTINCAO"
	else:
		mensagem="LIMITE"
		
print(mensagem)
print(a)
	