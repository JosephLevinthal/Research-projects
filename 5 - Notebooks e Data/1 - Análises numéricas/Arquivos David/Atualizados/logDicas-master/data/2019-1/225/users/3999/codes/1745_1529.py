Qinf=int(input("Quantidade infantaria: "))
Qcav=int(input("Quantidade cavalaria: "))
Pi=float(input())/100
Pc=float(input())/100
t=0
Qtinf=Qinf+(Qinf*Pi)
Qtcav=Qcav+(Qcav*Pc)
while(Qtinf+Qtcav<50000):
	t=t+1
	Qt= Qinf+(Qinf*Pi)+Qcav+(Qcav*Pc)

	print(t)