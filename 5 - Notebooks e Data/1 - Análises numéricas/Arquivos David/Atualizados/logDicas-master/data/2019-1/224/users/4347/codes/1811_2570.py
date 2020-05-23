from numpy import*
x=array(eval(input("valores: ")))
t=sum(x)/size (x)
h=1
for i in x:
	h=h*(i-t)
	h=abs(h)
print (round(h**(1/size(x)),3))