from numpy import*
v=array(eval(input("insira os vetores: ")))
i=0
while i!=size(v):
	a=v[i]
	if not(a%2==0):
		v[i]=0
	i=i+1
print(v)