from numpy import*
x=array(eval(input("digite o tempo ")))
h=0
while(size(x)>h):
	if(x[h]==min(x)):
		t=h
		h=1000
	else:
		h=h+1
print(t)
			


