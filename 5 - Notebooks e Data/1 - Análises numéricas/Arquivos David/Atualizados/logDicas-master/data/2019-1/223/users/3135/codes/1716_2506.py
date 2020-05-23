anos=0
quant= float(input("Quantidade inicial de tambaqui:"))
p_cres=float(input("Insira o percentual de crescimento:"))
venda=float(input("Insira a quantidade pra venda:"))

while (0<quant<12000):
	acre = quant * p_cres/ 100
	quant+=acre	
	quant-=venda		
	anos+=1

if(quant<=0):
	print("EXTINCAO")
else:
	print("LIMITE")
print(anos)