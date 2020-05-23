Qi=int(input())
Pc=float(input())
Qv=int(input())
t=0
a=Qi
while(a>0) and	 (a<12000) and (Pc>0) and (Qv>0):
	t=t+1
	a=a+(a*(Pc/100))
	a= a-Qv
if(a>=12000):
	print("LIMITE")
	print(t)
else:
	print("EXTINCAO")
	print
	