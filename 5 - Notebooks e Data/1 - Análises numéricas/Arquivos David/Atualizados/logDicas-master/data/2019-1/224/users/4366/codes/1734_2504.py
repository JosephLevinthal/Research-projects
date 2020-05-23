quant1=int(input("digite a quantidade inicial de copias:"))
quant2=int(input("digite a quantidade inicial de leucocitos:"))
p1=int(input("digite o percentual1:"))
p2=int(input("digite o percentual2:"))
p1=p1/100
p2=p2/100
t=0
while(2*quant1>quant2):
	quant1=quant1+quant1*p1
	quant2=quant2+quant2*p2
	t=t+1
print(t)









