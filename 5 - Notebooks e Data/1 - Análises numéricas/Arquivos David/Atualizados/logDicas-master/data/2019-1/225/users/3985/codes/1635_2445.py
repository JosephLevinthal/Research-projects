var= input("Variavel: ")

if(var == "C"):
	g= float(input())
	print(round((g*1.8)+32, 2))
else:
	h= float(input())
	print(round((h-32)/1.8, 2))