from numpy import *
gp = array(eval(input()))
gc = array(eval(input()))
v = e = d = i = 0
for i in range(0,len(gp)):
	if gp[i]<gc[i]:
		d+=1
	if gp[i]>gc[i]:
		v+=1
	if gp[i]==gc[i]:
		e+=1
g = array([v,e,d])
print(g)