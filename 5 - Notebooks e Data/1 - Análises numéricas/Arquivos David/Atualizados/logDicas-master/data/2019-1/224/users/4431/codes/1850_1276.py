from numpy import*
x=array(eval(input("Digite a matriz: ")))
t=zeros(7,dtype=int)

for i in range(7):
	t[i]=sum(x[:,i])
for i in range(7):
	if t[i] == max(t):
		print(i+1)