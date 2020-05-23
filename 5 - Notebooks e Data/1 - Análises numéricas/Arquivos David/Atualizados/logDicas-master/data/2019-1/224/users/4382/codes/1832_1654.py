from numpy import *
x = input("digite : ")
v = x.split(',')
z = zeros(5,dtype = int)
for i in v:
	if(i == "AM"):
		z[0] = z[0] + 1
	if(i == "PE"):
		z[1] = z[1] + 1
	if(i == "MG"):
		z[2] = z[2] + 1
	if(i == "SP"):
		z[3] = z[3] + 1
	if(i == "RS"):
		z[4] = z[4] + 1
print(max(z))
print(z)
			 
	 
