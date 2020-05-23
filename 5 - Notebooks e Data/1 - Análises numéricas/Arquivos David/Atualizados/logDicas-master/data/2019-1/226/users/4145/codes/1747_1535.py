x = float(input("valor de x: "))
k = int(input("numero de repeticoes: "))
i = 0
#s=((x**(2*i+ 1))/(2*i +1))*(-1)**i
s=0
while((-1<=x<=1)and(k>0)):
	s= s + ((x**(2*i +1))/(2*i +1))*(-1)**i
	i=i+1
	k=k-1
print(round(s,6))