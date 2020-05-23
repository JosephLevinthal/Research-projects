tem=input("temperatura em C ou F?: ")
val=float(input("valor da temperatura: "))
x=tem.upper()
c=5/9*(val-32)
f=1.8*val+32
if(x=="C"):
	men=f
else:
	men=c
print(round(men,2))	