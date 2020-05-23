from numpy import *
faltas = array(eval(input("digite as semanas de falta: ")))
s,t,q,qi,sex,sab = 0,0,0,0,0,0
for pos in faltas:
	if(pos == 2):
		s = s + 1
	if(pos == 3):
		t = t + 1
	if(pos == 4):
		q = q + 1
	if(pos == 5):
		qi = qi + 1
	if(pos == 6):
		sex = sex + 1
	if(pos == 7):
		sab = sab + 1
z = zeros(6,dtype = float)
z[0] = round((s/size(faltas)) * 100,1)
z[1] = round((t/size(faltas)) * 100,1)
z[2] = round((q/size(faltas)) * 100,1)
z[3] = round((qi/size(faltas)) * 100,1)
z[4] = round((sex/size(faltas)) * 100,1)
z[5] = round((sab/size(faltas)) * 100,1)
print(z)
