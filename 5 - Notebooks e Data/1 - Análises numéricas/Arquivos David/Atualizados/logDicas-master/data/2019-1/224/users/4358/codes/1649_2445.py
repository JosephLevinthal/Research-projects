escolha=input("escolha, C OU f:")
temp=float(input("valor da temperatura:"))
c1=(5/9)*(temp-32)
c2=(temp*9/5)+32
if(escolha=="C"):
	print(round(c2,2))
else:
	print(round(c1,2))
	
