from numpy import *
pal = input("digite a frase: ")
copy = ""
i = 0

while(i<len(pal)):
	if(pal[i] == " "):
		copy = copy + ""
	else:
		copy = copy + str(pal[i])
	i = i + 1
print(copy.upper())
valor = 0
i2 = 0

while(i2<len(copy)):
	if(copy[i2] == copy[-1*(i2+1)]): 
		valor = valor + 1             
	else:
		valor = valor + 0
	i2 = i2 + 1

if(valor == len(copy)):
	print("1")
else:
	print("0")
