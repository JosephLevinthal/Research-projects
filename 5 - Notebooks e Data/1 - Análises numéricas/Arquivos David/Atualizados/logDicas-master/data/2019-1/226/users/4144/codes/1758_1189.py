from numpy import *
a = input("digite a palavra: ")
new = a.replace("","")
inv = ""
i = -1
while(i>= -len(new)):
	inv = inv + new[i]
	i = i - 1
print(new.upper())
if(inv == new):
	print(1)
else:
	print(0)