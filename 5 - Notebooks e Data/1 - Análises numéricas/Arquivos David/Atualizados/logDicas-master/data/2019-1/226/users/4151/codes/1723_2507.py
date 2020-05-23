qi=int(input("quantidade de peixe no tanque: "))
pc=int(input("percentual de crescimento: "))/100
#v=int(input("venda mensal: "))
t=0
while(qi>0 and qi<8000):
	v=int(input("venda mensal: "))
	qi=(qi+(qi*pc))-v
	t=t+1
	
if(qi<=0):
	print("ZERO")
else:
	print("MAXIMO")

print(t)

