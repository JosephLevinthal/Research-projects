# Ao testar sua solução, não se limite ao caso de exemplo.
from math import*
X=float(input(""))
Y=float(input(""))
Q1=X>0 and Y>0
Q2=Y>0 and X<0
Q3=X<0 and Y<0
Q4=Y<0 and X>0
if((X and Y >Q1) or (X and Y>Q2)):
	d="Superiores"
else:
	d="Inferiores"
print(d)	
