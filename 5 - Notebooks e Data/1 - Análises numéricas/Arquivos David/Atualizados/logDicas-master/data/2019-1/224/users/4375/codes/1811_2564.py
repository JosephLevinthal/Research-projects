from numpy import*
gols=array(eval(input("gols: ")))
adv=array(eval(input("adversario: ")))
x=zeros(3, dtype=int)
for i in range (size(gols)):
	if(gols[i]>adv[i]):
		x[0]=x[0]+1
	if(gols[i]<adv[i]):
		x[2]=x[2]+1
	if(gols[i]==adv[i]):
		x[1]=x[1]+1


print(x)
