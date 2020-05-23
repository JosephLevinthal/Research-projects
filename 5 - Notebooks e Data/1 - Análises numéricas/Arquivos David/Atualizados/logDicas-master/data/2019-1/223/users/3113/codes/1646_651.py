a=float(input("altura:"))
s=input("M/F:")

g1=(72.7*a)-58
g2=(62.1*a)-44.7

if(s.upper()=="M"):
	po=g1
else:
	po=g2
print(round(po,2))	
