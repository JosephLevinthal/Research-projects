v=int(input("quantidade inicial de copias de virus: "))
l=int(input("quantidade de leucocitos: "))
pv=int(input("percetual de virus: "))/100
pl=int(input("percentual de leucocitos: "))/100

t=0
while(l<2*v):
	v=v+(v*pv)
	l=l+(l*pl)
	t=t+1
print(t)
	
	
	