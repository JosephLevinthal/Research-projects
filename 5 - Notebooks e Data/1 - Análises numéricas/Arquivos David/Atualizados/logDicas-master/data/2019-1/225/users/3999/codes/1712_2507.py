Qi=int(input())
p1=float(input())
a=Qi
t=0
while(a<8000) and (a>0):
	t=t+1
	Qv=int(input())
	a=a+(a*(p1/100))
	a= a-Qv
if(a>=8000):
	print("MAXIMO")
else:
	print("ZERO")
print(t)	