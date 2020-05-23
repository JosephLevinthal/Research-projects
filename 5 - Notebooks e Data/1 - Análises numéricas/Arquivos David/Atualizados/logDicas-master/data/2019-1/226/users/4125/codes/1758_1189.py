from numpy import*
n = input("digite uma string: ")
nova = n.replace(" "," ")
inv = ""
i = -1
while(i>= -len(nova)):
	inv = inv + nova[i]
	i = i -1
print(nova.upper())
if nova == inv :
	print(1)
else: 
	print(0)