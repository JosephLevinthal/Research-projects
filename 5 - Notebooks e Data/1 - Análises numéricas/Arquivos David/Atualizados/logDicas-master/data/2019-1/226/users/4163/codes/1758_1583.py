from numpy import*
a = input("digite: ")
i = 0 
b = len(a)%3
new = ""
while(i<len(a)):
	if(i % 3 == 0):
		new = new + "." + a[i] + a[i+1] + a[i+2]
	else:
		new = new
	i = i +1
r = new[1:]
print(r)

		