from numpy import*

md=array(eval(input("")))   #média
pre=array(eval(input("")))  #presença
ch=int(input(""))   #carga horária

a=zeros(3,dtype=int)

for i in range(size(md)):      #sempre usar o range
	if (md[i]>=5)and (pre[i] >= ch*0.75):
		a[0]+=1
	if (md[i]<5) and( pre[i] >= ch*0.75):
		a[1]+=1
	if (md[i]>=5)and (pre[i] < ch*0.75):
		a[2]+=1
print(a)

