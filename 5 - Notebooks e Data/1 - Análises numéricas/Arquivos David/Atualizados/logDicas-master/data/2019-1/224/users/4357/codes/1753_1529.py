qinf=int(input("digite o numero:"))
qcav=int(input("digite o numero:"))
pinf=float(input("digite o numero:"))
pcav=float(input("digite o numero:"))
pinf=pinf/100
pcav=pcav/100
mes=0
total=qinf+qcav
while(0<=total<=50000):
	qinf=qinf+qinf*pinf
	qcav=qcav+qcav*pcav
	total=qinf+qcav
	mes=mes+1
print(mes)
