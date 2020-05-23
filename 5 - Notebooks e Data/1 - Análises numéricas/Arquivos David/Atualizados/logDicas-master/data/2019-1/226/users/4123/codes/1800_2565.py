from numpy import *
mf = array(eval(input()))
pr = array(eval(input()))
ch = float(input())
a = rf = rn = x =  0
for x in range (0,len(mf)):
	if mf[x]<5:
		rn+=1
	elif pr[x]/ch<0.75:
		rf+=1
	else:
		a+=1
g = array([a,rn,rf])
print(g)