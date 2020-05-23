from numpy import *
v = array(eval(input("dias: ")))
r = zeros(6, dtype=float)
for i in range(size(v)):
	if(v[i]==2):
		r[0]=r[0]+1
	elif(v[i]==3):
		r[1]=r[1]+1
	elif(v[i]==4):
		r[2]=r[2]+1
	elif(v[i]==5):
		r[3]=r[3]+1
	elif(v[i]==6):
		r[4]=r[4]+1
	elif(v[i]==7):
		r[5]=r[5]+1
d = sum(r)
for f in range(size(r)):
	 r[f]=round((r[f]/d)*100, 1)
print(r)





