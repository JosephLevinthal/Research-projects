nA=int(input("numero de habitantes da cidade A:"))
nB=int(input("numero de habitantes da cidade B:"))
cpA= float(input("crescimento populacional ds cidade A:"))
cpB= float(input("crescimento populacional ds cidade B:"))
t=0
xA=nA
xB=nB
while(xA<=xB) and (cpA>cpB):
	xA=xA+(xA*(cpA/100))
	xB=xB+(xB*(cpB/100))
	t=t+1
print(t)