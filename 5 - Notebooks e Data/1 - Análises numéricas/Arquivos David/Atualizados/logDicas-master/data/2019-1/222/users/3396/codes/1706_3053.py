from math import*
p= int(input("p:"))
if(p>= 0 or p< 5000):
	v= p*0.03+20.00
	print(v)
elif(p>= 5000 or p<6000):
	v= p*0.04+25.00
	print(v)
elif(p>=6000 or p<7000):
	v= p*0.05+30.00
	print(v)
elif(p>= 7000):
	v= p*0.06+35.00
	print(v)
	
	