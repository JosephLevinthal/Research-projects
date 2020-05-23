from numpy import*
x=array(eval(input("Digite os valores: ")))
t=sum(x)/size(x)
h=0
for i in x:
	h=h+((i-t)**2)
h=(h/(size(x)-1))**0.5
print(round(h,3))