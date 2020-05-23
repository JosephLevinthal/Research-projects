g=int(input("quantidade inicial:"))
p=float(input("percentual de crescimento:"))
r=int(input("retirados/ano:"))

t=0
while(g<12000 and g>0):
	j=(g*p)/100
	g=g+j-r
	t=t+1
if(g>=12000):
	i="LIMITE"
	print(i)
elif(g<=0):
	i="EXTINCAO"
	print(i)
print(t)
