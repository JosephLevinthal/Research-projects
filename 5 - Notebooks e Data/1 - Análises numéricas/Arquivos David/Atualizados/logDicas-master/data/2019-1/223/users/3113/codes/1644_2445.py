T=input("C/F?:")
s=float(input("temperatura:"))


C=(s*9/5)+32
F=(s-32)*5/9

if(T.upper()=="C"):
	t=C
else:
	t=F
print(round(t,2))