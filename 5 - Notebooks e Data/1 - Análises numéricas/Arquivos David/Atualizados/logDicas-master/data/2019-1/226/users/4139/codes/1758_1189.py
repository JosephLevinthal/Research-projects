from numpy import*
palavra = input("digite a palavra: ")

nova = palavra.replace(" ","")
contrario = ""
i = - 1
while(i >= -len(nova)):
	contrario = contrario + nova[i]
	i = i - 1
print(nova.upper())
if(contrario == nova):
	print(1)
else:
	print(0)