quan1=int(input("quantidade inicial: "))
pc = int(input("percentual de crescimento: "))
quanv= int(input("quantidade para vendas anuais: "))

a = pc/100
ano = 0 

while (quan1>0)and(quan1<12000):
	quan1 += (quan1*a)
	quan1 = quan1 - quanv
	ano = ano+1

if(quan1>12000):	
	print("LIMITE")
if(quan1<0):
	print("EXTINCAO")
	
	
print(ano)