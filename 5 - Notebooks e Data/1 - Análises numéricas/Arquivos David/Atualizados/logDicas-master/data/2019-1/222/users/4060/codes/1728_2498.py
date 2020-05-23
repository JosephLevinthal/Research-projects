a=int(input("numero de habitantes a: "))
b=int(input("numero de habitantes b: "))
pa=float(input("porcentual a: "))
pb=float(input("porcentual b: "))
va=a
vb=b
t=0
while(va<vb):	
	pcpa=va*(pa/100) #calculo porcentual crescimento de a
	va=pcpa+va
	pcpb=vb*(pb/100) #calculo porcentual crescimento de b
	vb=pcpb+vb
	t=t+1
print(t)
	

