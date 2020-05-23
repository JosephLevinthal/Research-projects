r=float(input());
x=float(input());
opcao=int(input());
from math import *
if(opcao==1):
	
	v=((pi*x**2)*((3*r)-x))/3
	print(round(v,4));
if(opcao==2):
	v=(4*pi*r**3)/3 - ((pi*x**2)*((3*r)-x))/3;
	print(round(v,4));