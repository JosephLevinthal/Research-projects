escala=(input("C/F:"))
temp=float(input("temp:"))
C1= (temp-32)*5/9
c2=(temp*9/5)+32
if(escala=="F"):
	print(round(C1,2))
if(escala=="C"):
	print(round(c2,2))