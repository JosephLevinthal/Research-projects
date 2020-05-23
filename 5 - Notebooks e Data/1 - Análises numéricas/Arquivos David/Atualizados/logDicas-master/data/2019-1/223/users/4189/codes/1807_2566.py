from numpy import*

fa=array(eval(input("")))

a=zeros(6)

for i in range(size(fa)):
	if fa[i]==2:
		a[0]+=1
	if fa[i]==3:
		a[1]+=1
	if fa[i]==4:
		a[2]+=1
	if fa[i]==5:
		a[3]+=1
	if fa[i]==6:
		a[4]+=1
	if fa[i]==7:
		a[5]+=1
for i in range(size(a)):
	a[i]=round(a[i]/size(fa)*100,1)
	
print(a)

	  