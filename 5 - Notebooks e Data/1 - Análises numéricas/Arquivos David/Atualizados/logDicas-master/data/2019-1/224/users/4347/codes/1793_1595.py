from numpy import*
n=array(eval(input("nota dos alunos")))
h=0
t=0
while(size(n)>h):
	t=t+n[h]
	h=h+1
t=t-min(n)
y=size(n)
y=y-1
t=t/y
print(round(t,2))
	











