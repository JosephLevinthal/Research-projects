from numpy import*
t=array(eval(input("Digite a matriz: ")))
v=t.shape[0]
o=zeros(v,dtype=float)
k=zeros(v,dtype=float)
for i in range(0,v):
	u=t[i,0]
	o[i]=u
for i in range(0,v):
	n=t[i,1]
	k[i]=n
b=zeros(v,dtype=float)

for i in range(0,v):
	b[i]=o[i]*k[i]
y=round(sum(b)/v,2)

print(y)
