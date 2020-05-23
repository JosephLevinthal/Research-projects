from numpy import*
x = input("digite a string: ")
y = ""
for i in range(len(x)):
	if(x[i]!="a")and(x[i]!="A"):
		y = y + x[i]
print(y)