from numpy import*
a=array(eval(input("x: ")))

i=0
j=0

while j<size(a):
	if a[j]>99:
		print(j)
		i=i+1
	j=j+1
print(i)