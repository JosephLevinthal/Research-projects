v=float(input("valor:"))

if(v<=300.00):
	valortotal=(v*10/100)+v
	print(round(valortotal,2))
else:	
	valortotal=(v*6/100)+v
	print(round(valortotal,2))
	