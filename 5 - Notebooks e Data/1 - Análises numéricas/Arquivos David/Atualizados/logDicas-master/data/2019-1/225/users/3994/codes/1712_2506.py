q=int(input("Quantidade inicial: "))
p=int(input("percentual de crescimento: "))
r=int(input("qtd retirada todos os anos: "))
t=0
while(q<12000 and q>0):
	h=(q*p)/100
	q=q+h-r
	t+=1
if(q>=12000):
	print("LIMITE")
elif(q<=0):
	print("EXTINCAO")
print(t)
	

