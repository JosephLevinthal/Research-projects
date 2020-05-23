from numpy import*
x=array(eval(input("Digite a matriz: ")))
h=shape(x)[0]
t=zeros(h,dtype=int)

for i in range(h):
	t[i]=sum(x[i,:])
print(t)	