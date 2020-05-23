num = int(input("Digite um numero: "))
pc = int(input("percentual de crescimento: "))
quanv= int(input(" vendas anuais: "))

a = pc/100
ano = 0 

while (num>0)and(num<=8000):
	num = num + (num * a)
	num = num - quanv
	ano = ano+1

	
if(num>=8000):	
	print("MAXIMO")
if(num<=0):
	print("ZERO")
	num = int(input("vendas anuais: "))

print(ano)
	
