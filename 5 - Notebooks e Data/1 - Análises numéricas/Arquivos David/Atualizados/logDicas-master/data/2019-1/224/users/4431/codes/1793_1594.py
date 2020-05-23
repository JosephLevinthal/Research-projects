from numpy import*
x=array(eval(input("Digite os golpes: ")))
h=0
f=1
t=0
while(size(x)>h):
	t=t+x[h]*f
	f=f+1
	h=h+1


print(t)