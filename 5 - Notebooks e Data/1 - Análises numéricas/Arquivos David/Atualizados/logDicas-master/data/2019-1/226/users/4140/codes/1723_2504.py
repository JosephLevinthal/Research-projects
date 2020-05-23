#quando as celulas de defesa forem forem o dobro da quantidade de virus 
vinicial=int(input())
linicial=int(input())
percentualv=float(input())
percentuall=float(input())
i=0
v=vinicial
l=linicial
while(l<v*2):
	somal=l*(percentuall/100)
	l=somal+l
	somav=v*(percentualv/100)
	v=v+somav
	i=i+1
print(i)
	