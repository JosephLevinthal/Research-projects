from numpy import*
x=array(eval(input("tempos: ")))
y=array(eval(input("percentual: ")))
h=0
t=0
while(size(x)>h):
	t=t+(x[h]*(y[h]/100))
	h=h+1
t=t*5
print(round(t, 2))