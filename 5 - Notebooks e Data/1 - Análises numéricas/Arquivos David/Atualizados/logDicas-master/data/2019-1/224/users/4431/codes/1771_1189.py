x=input("Digite algo: ")
x=x.replace(" ","")
print(x.upper())



y=""
i=-1
while(i>=-len(x)):
	y=y+x[i]
	i=i-1
if(y==x):
	print("1")
else:
	print("0")