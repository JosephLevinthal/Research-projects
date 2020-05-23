g=int(input("quantidade inicial:"))
p=float(input("percentual de crescimento:"))


t=0
while(g<8000 and g>0):
	r=int(input("retirados/ano:"))
	j=(g*p)/100
	g=g+j-r
	t=t+1
if(g>=8000):
	i="MAXIMO"
	print(i)
elif(g<=0):
	i="ZERO"
	print(i)
print(t)
