from numpy import*
g= array(eval(input("insira o valor da glicose: ")))
i=0
s=0
while i!=size(g):
	if g[i]>99:
		print(i)
		s=s+1
	i=i+1
print(s)