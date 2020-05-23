grandeza=input().upper()
valor=float(input())

if(grandeza=="C"):
	F=(9*valor+160)/5;
	print(round(F,2))
if(grandeza=="F"):
	C=(5*valor-160)/9
	print(round(C,2))