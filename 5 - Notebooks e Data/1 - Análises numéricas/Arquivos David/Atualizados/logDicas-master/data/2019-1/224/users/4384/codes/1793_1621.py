from numpy import *
P=array(eval(input("produtos: ")))
q=array(eval(input("quantidade: ")))
c=array(eval(input("comprado: ")))	
if(c[1]=="ARROZ"):
	a=1.25*q[1]
elif(c[2]=="FANTA"):
	b=3.20*q[3]
elif(c[3]=="BIS"):
	d=1.80*q[3]
h=a+b+d
print(h)