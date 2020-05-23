p=float(input("percurso:"))
t=input("tipo:")

#8 km com 1 litro tipo A.
s=p/8*1
#12 ___________________B.
d=p/12*1
if(t.upper()=="A"):
	p=s
else:
	p=d
print(round(p,2))